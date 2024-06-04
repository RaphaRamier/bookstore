from django.urls import path
from books.views import BookCreateListView, BookRetrieveUpdateDestroy


urlpatterns = [
    path('books/', BookCreateListView.as_view(), name='book-create-list'),
    path('books/<int:pk>', BookRetrieveUpdateDestroy.as_view(), name='book-detail-view'),
]