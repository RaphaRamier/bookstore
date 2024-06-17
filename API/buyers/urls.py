from django.urls import path
from API.buyers.views import BuyerCreateListView, BuyerRetrieveUpdateDestroy, BuyerStatisticsView

urlpatterns = [
    path('buyers/', BuyerCreateListView.as_view(), name='buyer-create-view'),
    path('buyers/<int:pk>', BuyerRetrieveUpdateDestroy.as_view(), name='buyer-detail-view'),
    path('buyers/statistics/', BuyerStatisticsView.as_view(), name='buyer-statistics'),

]