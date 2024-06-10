from django.urls import path
from API.suppliers.views import SupplierCreateListView, SupplierRetrieveUpdateDestroy, SupplierStatisticsView

urlpatterns = [
    path('suppliers/', SupplierCreateListView.as_view(), name='supplier-create-view'),
    path('supplier/<int:pk>', SupplierRetrieveUpdateDestroy.as_view(), name='supplier-detail-view'),
    path('suppliers/statistics/', SupplierStatisticsView.as_view(), name='supplier-statistics'),

]