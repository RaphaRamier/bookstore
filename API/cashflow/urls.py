from django.urls import path
from .views import (
    CashFlowView,
    CashInFlowCreateListView,
    CashInFlowRetrieveUpdateDestroyView,
    CashOutFlowCreateListView,
    CashOutFlowRetrieveUpdateDestroyView
)

urlpatterns=[
    path('cashflow/', CashFlowView.as_view(), name='cashflow-detail'),
    path('cashflow/inflow/', CashInFlowCreateListView.as_view(), name='inflow-create-list'),
    path('cashflow/inflow/<int:pk>', CashInFlowRetrieveUpdateDestroyView.as_view(), name='inflow-detail-view'),
    path('cashflow/outflow/', CashOutFlowCreateListView.as_view(), name='outflow-create-list'),
    path('cashflow/outflow/<int:pk>', CashOutFlowRetrieveUpdateDestroyView.as_view(), name='outflow-detail-view'),

]
