from django.urls import path
from API.services.views import ServiceCreatListView, ServiceRetrieveUpdateDestroyView


urlpatterns = [
    path('services/', ServiceCreatListView.as_view(), name='service-create-list'),
    path('services/<int:pk>', ServiceRetrieveUpdateDestroyView.as_view(), name='service-detail.view'),

]
