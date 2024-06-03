from django.urls import path
from suppliers.views import SupplierCreateListView, SupplierRetrieveUpdateDestroy

urlpatterns = [
    path('suppliers/', SupplierCreateListView.as_view(), name='supplier-create-view'),
    path('supplier/<int:pk>', SupplierRetrieveUpdateDestroy.as_view(), name='supplier-detail-view')
]