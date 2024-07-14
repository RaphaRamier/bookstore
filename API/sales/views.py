from django.db.models import Count, Sum
from django.db.models.functions import TruncMonth, TruncYear, TruncDay
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


class SaleDailyTrendView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        queryset = Sale.objects.filter(status='SUCCESSFUL')

        daily_trends = queryset.annotate(
            day=TruncDay('sale_date')
        ).values('day').annotate(
            total_quantity=Sum('quantity'),
            total_value=Sum('total_value')
        ).order_by('day')

        daily_df = pd.DataFrame(list(daily_trends))

        daily_df['percentage_difference'] = daily_df['total_value'].astype(float).pct_change() * 100
        daily_df['cumulative_percentage'] = ((1 + daily_df['percentage_difference'] / 100).cumprod()) - 1

        daily_df = daily_df.replace([float('inf'), -float('inf'), float('nan')], 0)

        daily_data = [
            {
                'day': entry['day'].strftime('%Y-%m-%d'),
                'total_quantity': entry['total_quantity'],
                'total_value': entry['total_value'],
                'percentage_difference': round(row['percentage_difference'], 2) if pd.notna(row['percentage_difference']) else None,
                'cumulative_percentage': round(row['cumulative_percentage'], 2) if pd.notna(row['cumulative_percentage']) else 0
            }
            for i, (entry, row) in enumerate(zip(daily_trends, daily_df.to_dict('records')))
        ]

        genres_trend = queryset.annotate(
            day=TruncDay('sale_date')
        ).values('day', 'book__book__genres__name').annotate(
            total_quantity=Sum('quantity'),
            total_value=Sum('total_value')
        ).order_by('-day', 'book__book__genres__name')

        genre_df = pd.DataFrame(list(genres_trend))

        genre_df['percentage_difference'] = genre_df['total_value'].astype(float).pct_change() * 100
        genre_df['cumulative_percentage'] = ((1 + genre_df['percentage_difference'] / 100).cumprod()) - 1

        genre_df = genre_df.replace([float('inf'), -float('inf'), float('nan')], 0)

        genres_data = [
            {
                'day': entry['day'].strftime('%Y-%m-%d'),
                'genre': entry['book__book__genres__name'],
                'total_quantity': entry['total_quantity'],
                'total_value': round(entry['total_value'], 2),
                'percentage_difference': round(row['percentage_difference'], 2) if pd.notna(row['percentage_difference']) else None,
                'cumulative_percentage': round(row['cumulative_percentage'], 2) if pd.notna(row['cumulative_percentage']) else 0
            }
            for i, (entry, row) in enumerate(zip(genres_trend, genre_df.to_dict('records')))
        ]

        data = {
            'daily_trends': daily_data[::-1],
            'genres_trend': genres_data[::-1],
        }

        return Response(data)



class SaleMonthlyTrendView(APIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission)
    queryset = Sale.objects.filter(status='SUCCESSFUL')

    def get(self, request):
        monthly_trends = self.queryset.annotate(
            month=TruncMonth('sale_date')
        ).values('month').annotate(
            total_quantity=Sum('quantity'),
            total_value=Sum('total_value')
        ).order_by('month')

        df = pd.DataFrame(list(monthly_trends))

        df['percentage_difference'] = df['total_value'].pct_change() * 100

        monthly_data = [
            {
                'month': entry['month'].strftime('%Y-%m'),
                'total_quantity': entry['total_quantity'],
                'total_value': entry['total_value'],
                'percentage_difference': round(row['percentage_difference'], 2) if pd.notna(row['percentage_difference']) else None,
            }
            for i, (entry, row) in enumerate(zip(monthly_trends, df.to_dict('records')))
        ]

        monthly_revenue_dict = {entry['month']: entry['total_value'] for entry in monthly_data}

        genres_trend = self.queryset.filter(status='SUCCESSFUL').annotate(
            month=TruncMonth('sale_date')
        ).values('month', 'book__book__genres__name').annotate(
            total_quantity=Sum('quantity'),
            total_value=Sum('total_value')
        ).order_by('-month', 'book__book__genres__name')

        genres_data = [
            {
                'month': entry['month'].strftime('%Y-%m'),
                'genre': entry['book__book__genres__name'],
                'total_quantity': entry['total_quantity'],
                'total_value': entry['total_value'],
                'revenue': round((entry['total_value'] / monthly_revenue_dict[entry['month'].strftime('%Y-%m')]) * 100, 2)
            }
            for entry in genres_trend
        ]

        data = {
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
