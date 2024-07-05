from django.urls import path
from API.sales.views import SaleCreateListView, SaleRetrieveUpdateDestroy, SaleMonthlyTrendView, SaleYearlyTrendView, \
    SaleDailyTrendView

urlpatterns = [
    path('sales/', SaleCreateListView.as_view(), name='sale-create-list'),
    path('sales/<int:pk>', SaleRetrieveUpdateDestroy.as_view(), name='sale-detail.view'),
    path('sales/monthly-trend/', SaleMonthlyTrendView.as_view(), name='monthly-trend'),
    path('sales/daily-trend/', SaleDailyTrendView.as_view(), name='daily-trend'),
    path('sales/yearly-trend/', SaleYearlyTrendView.as_view(), name='yearly-trend'),

]