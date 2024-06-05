from django.urls import path
from components.views import ComponentCreateListView, ComponentRetrieveUpdateDestroy, SupplyMonthlyTrendView, SupplyYearlyTrendView

urlpatterns = [
    path('components/', ComponentCreateListView.as_view(), name='component-list-create'),
    path('components/<int:pk>/', ComponentRetrieveUpdateDestroy.as_view(), name='component-detail'),
    path('components/statistics/monthly/', SupplyMonthlyTrendView.as_view(), name='components-statistics-month'),
    path('components/statistics/yearly/', SupplyYearlyTrendView.as_view(), name='components-statistics-year')
]