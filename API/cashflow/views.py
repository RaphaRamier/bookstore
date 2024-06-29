from django.db.models import Sum
from django.db.models.functions import TruncMonth
from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from setup.permissions import GlobalDefaultPermission
from .models import CashInFlow, CashOutFlow
from rest_framework import generics
from .serializers import CashInFlowSerializer, CashOutFlowSerializer
from ..sales.models import Sale


class CashInFlowCreateListView(generics.ListCreateAPIView):
    permission_classes=(IsAuthenticated, GlobalDefaultPermission)
    queryset=CashInFlow.objects.all()
    serializer_class=CashInFlowSerializer


class CashInFlowRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=(IsAuthenticated, GlobalDefaultPermission)
    queryset=CashInFlow.objects.all()
    serializer_class=CashInFlowSerializer


class CashOutFlowCreateListView(generics.ListCreateAPIView):
    permission_classes=(IsAuthenticated, GlobalDefaultPermission)
    queryset=CashOutFlow.objects.all()
    serializer_class=CashOutFlowSerializer


class CashOutFlowRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=(IsAuthenticated, GlobalDefaultPermission)
    queryset=CashOutFlow.objects.all()
    serializer_class=CashOutFlowSerializer


class CashFlowView(APIView):
    permission_classes=(IsAuthenticated, GlobalDefaultPermission)

    def get(self, request):
        total_inflow=CashInFlow.objects.filter(source__status='SUCCESSFUL').aggregate(total=Sum('amount'))['total'] or 0
        total_pending=CashInFlow.objects.filter(source__status='PENDING').aggregate(total=Sum('amount'))['total'] or 0
        total_outflow=CashOutFlow.objects.aggregate(total=Sum('amount'))['total'] or 0
        cash_flow=total_inflow - total_outflow

        data={
            'total_inflow': total_inflow,
            'total_pending': total_pending,
            'total_outflow': total_outflow,
            'cash_flow': cash_flow
        }
        return Response(data)


class PerformanceDataView(APIView):

    def get(self, request):
        monthly_sales=Sale.objects.filter(status='SUCCESSFUL').annotate(
            month=TruncMonth('sale_date')
        ).values('month').annotate(
            total_value=Sum('total_value')
        ).order_by('month')

        sales_data={
            'dates': [entry['month'].strftime('%Y-%m') for entry in monthly_sales],
            'revenues': [entry['total_value'] for entry in monthly_sales]
        }

        monthly_expenses=CashOutFlow.objects.annotate(
            month=TruncMonth('date')
        ).values('month').annotate(
            total_value=Sum('amount')
        ).order_by('month')

        expenses_data={
            'dates': [entry['month'].strftime('%Y-%m') for entry in monthly_expenses],
            'expenses': [entry['total_value'] for entry in monthly_expenses]
        }

        all_dates=sorted(set(sales_data['dates']) | set(expenses_data['dates']))

        performance_data={
            'dates': all_dates,
            'revenues': [sales_data['revenues'][sales_data['dates'].index(date)] if date in sales_data['dates'] else 0
                         for date in all_dates],
            'expenses': [
                expenses_data['expenses'][expenses_data['dates'].index(date)] if date in expenses_data['dates'] else 0
                for date in all_dates],
        }

        return Response(performance_data)
