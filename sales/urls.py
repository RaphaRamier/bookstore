from django.urls import path
from sales.views import SaleCreatListView, SaleRetrieveUpdateDestroyView


urlpatterns = [
    path('sales/', SaleCreatListView.as_view(), name='sale-create-list'),
    path('sales/<int:pk>', SaleRetrieveUpdateDestroyView.as_view(), name='sale-detail.view'),

]