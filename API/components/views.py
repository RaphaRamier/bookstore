from django.db.models import Sum
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models.functions import TruncMonth, TruncYear
from API.components.models import Component
from API.components.serializers import ComponentSerializer
from setup.permissions import GlobalDefaultPermission


class ComponentCreateListView(generics.ListCreateAPIView):
    permission_classes=(IsAuthenticated, GlobalDefaultPermission)
    queryset=Component.objects.all()
    serializer_class=ComponentSerializer


class ComponentRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=(IsAuthenticated, GlobalDefaultPermission)
    queryset=Component.objects.all()
    serializer_class=ComponentSerializer


class SupplyMonthlyTrendView(APIView):
    permission_classes=(IsAuthenticated, GlobalDefaultPermission)
    queryset=Component.objects.all()

    def get(self, request):

        monthly_trends=self.queryset.annotate(month=TruncMonth('date')).values('month').annotate(
            total_quantity=Sum('quantity'),
            total_value=Sum('price_total')
        ).order_by('month')

        data=[
            {
                'month': entry['month'].strftime('%Y-%m'),
                'total_quantity': entry['total_quantity'],
                'total_value': entry['total_value'],
            }
            for entry in monthly_trends
        ]

        return Response(data)


class SupplyYearlyTrendView(APIView):
    permission_classes=(IsAuthenticated, GlobalDefaultPermission)
    queryset=Component.objects.all()

    def get(self, request):
        yearly_trends=self.queryset.annotate(year=TruncYear('date')).values('year').annotate(
            total_quantity=Sum('quantity'),
            total_value=Sum('price_total')
        ).order_by('year')

        formatted_year=[
            {
                'date': entry['year'].strftime('%Y'),
                'total_quantity': entry['total_quantity'],
                'total_value': entry['total_value'],
            }
            for entry in yearly_trends
        ]

        data=formatted_year

        return Response(data)
