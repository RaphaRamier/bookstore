from django.urls import path
from .views import (
    CashFlowView,
    CashInFlowCreateListView,
    CashInFlowRetrieveUpdateDestroyView,
    CashOutFlowCreateListView,
    CashOutFlowRetrieveUpdateDestroyView, PerformanceDataView, SupplierMonthlyTrendView
)

urlpatterns=[
    path('cashflow/', CashFlowView.as_view(), name='cashflow-detail'),
    path('cashflow/inflow/', CashInFlowCreateListView.as_view(), name='inflow-create-list'),
    path('cashflow/inflow/<int:pk>', CashInFlowRetrieveUpdateDestroyView.as_view(), name='inflow-detail-view'),
    path('cashflow/outflow/', CashOutFlowCreateListView.as_view(), name='outflow-create-list'),
    path('cashflow/outflow/<int:pk>', CashOutFlowRetrieveUpdateDestroyView.as_view(), name='outflow-detail-view'),
    path('cashflow/performance-data/', PerformanceDataView.as_view(), name='performance-data'),
    path('cashflow/suppliers/monthly-trend/', SupplierMonthlyTrendView.as_view(), name='supplier_monthly_trend'),

]
