from django.urls import path
from components.views import ComponentCreateListView, ComponentRetrieveUpdateDestroy

urlpatterns = [
    path('components/', ComponentCreateListView.as_view(), name='component-list-create'),
    path('components/<int:pk>/', ComponentRetrieveUpdateDestroy.as_view(), name='component-detail'),
]