from django.urls import path
from API.sales.views import SaleCreateListView, SaleRetrieveUpdateDestroy


urlpatterns = [
    path('sales/', SaleCreateListView.as_view(), name='sale-create-list'),
    path('sales/<int:pk>', SaleRetrieveUpdateDestroy.as_view(), name='sale-detail.view'),

]