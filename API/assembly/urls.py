from django.urls import path
from API.assembly.views import BookAssemblyCreateListView, BookAssemblyRetrieveUpdateDestroyView

urlpatterns = [
    path('assembly/', BookAssemblyCreateListView.as_view(), name='assembly-create-list'),
    path('assembly/<int:pk>)', BookAssemblyRetrieveUpdateDestroyView.as_view(), name='assembly-detail-view')
]
