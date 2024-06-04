from django.urls import path
from authors.views import AuthorCreateListView, AuthorRetrieveUpdateDestroyView

urlpatterns = [
    path('authors/', AuthorCreateListView.as_view(), name='author-create-list'),
    path('authors/<int:pk>/', AuthorRetrieveUpdateDestroyView.as_view(), name='author-detail-view')
]
