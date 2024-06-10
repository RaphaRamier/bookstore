from django.urls import path
from API.books.views import BookCreateListView, BookRetrieveUpdateDestroy, BookStatisticsView

urlpatterns = [
    path('books/', BookCreateListView.as_view(), name='book-create-list'),
    path('books/<int:pk>', BookRetrieveUpdateDestroy.as_view(), name='book-detail-view'),
    path('books/statistics/', BookStatisticsView.as_view(), name='book-statistics')
]