from django.db.models import Count, Sum
from django.db.models.functions import TruncMonth, TruncYear
from django.http import JsonResponse
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from API.sales.models import Sale
from API.sales.serializers import SaleSerializer
from setup.permissions import GlobalDefaultPermission
import pandas as pd


class CustomPagination(PageNumberPagination):
    page_size=20
    page_size_query_param='page_size'
    max_page_size=100


class SaleCreateListView(generics.ListCreateAPIView):
    permission_classes=(IsAuthenticated, GlobalDefaultPermission)
    queryset=Sale.objects.all()
    serializer_class=SaleSerializer


class SaleRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=(IsAuthenticated, GlobalDefaultPermission)
    queryset=Sale.objects.all()
    serializer_class=SaleSerializer

    def delete(self, *args, **kwargs):
        instance=self.get_object()
        try:
            instance.delete()
            return JsonResponse({'message': 'Sale deleted successfully.'}, status=204)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)


class SaleMonthlyTrendView(APIView):
    permission_classes=(IsAuthenticated, GlobalDefaultPermission)
    queryset=Sale.objects.filter(status='SUCCESSFUL')

    def get(self, request):
        monthly_trends=self.queryset.annotate(
            month=TruncMonth('sale_date')
        ).values('month').annotate(
            total_quantity=Sum('quantity'),
            total_value=Sum('total_value')
        ).order_by('month')

        df=pd.DataFrame(list(monthly_trends))

        df['percentage_difference']=df['total_value'].pct_change() * 100

        monthly_data=[
            {
                'month': entry['month'].strftime('%Y-%m'),
                'total_quantity': entry['total_quantity'],
                'total_value': entry['total_value'],
                'percentage_difference': row['percentage_difference'] if i > 0 else None,
            }
            for i, (entry, row) in enumerate(zip(monthly_trends, df.to_dict('records')))
        ]

        genres_trend=self.queryset.filter(status='SUCCESSFUL').annotate(
            month=TruncMonth('sale_date')
        ).values('month', 'book__book__genres__name').annotate(
            total_quantity=Sum('quantity'),
            total_value=Sum('total_value')
        ).order_by('-month', 'book__book__genres__name')

        genres_data=[
            {
                'month': entry['month'].strftime('%Y-%m'),
                'genre': entry['book__book__genres__name'],
                'total_quantity': entry['total_quantity'],
                'total_value': entry['total_value'],
            }
            for entry in genres_trend
        ]

        data={
            'monthly_trends': monthly_data[::-1],
            'genres_trend': genres_data[::-1],
        }

        return Response(data)



class SaleYearlyTrendView(APIView):
    permission_classes=(IsAuthenticated, GlobalDefaultPermission)
    queryset=Sale.objects.all()

    def get(self, request):
        yearly_trends=self.queryset.filter(status='SUCCESSFUL').annotate(year=TruncYear('sale_date')).values(
            'year').annotate(
            total_quantity=Sum('quantity'),
            total_value=Sum('price_total')
        ).order_by('year')

        genres_trend=self.queryset.filter(status='SUCCESSFUL').annotate(month=TruncYear('sale_date')).values('year',
                                                                                                             'book__book__genres').annotate(
            total_quantity=Sum('quantity'),
            total_value=Sum('total_value')
        ).order_by('year', 'book__book__genres')

        genres_data=[
            {
                'month': entry['year'].strftime('%Y'),
                'total_quantity': entry['total_quantity'],
                'total_value': entry['total_value'],
            }
            for entry in genres_trend
        ]

        year_data=[
            {
                'date': entry['year'].strftime('%Y'),
                'total_quantity': entry['total_quantity'],
                'total_value': entry['total_value'],
            }
            for entry in yearly_trends
        ]

        data={
            'year_data': year_data,
            'genres_trend': genres_trend
        }

        return Response(data)
