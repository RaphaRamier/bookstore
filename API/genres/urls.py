from django.urls import path
from API.genres.views import GenreCreateListView, GenreRetrieveUpdateDestroyView, GenreStashView

urlpatterns = [
    path('genres/', GenreCreateListView.as_view(), name='genre-create-list'),
    path('genres/<int:pk>/', GenreRetrieveUpdateDestroyView.as_view(), name='genre-detail-view'),
    path('genres/stash/', GenreStashView.as_view(), name='genre-stash')
]