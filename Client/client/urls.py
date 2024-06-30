from django.urls import path
from Client.client.views import home, analytics, balance, add_book, book_shelf, book_detail, edit_book, authors_list, \
    books_by_genre, author_detail

urlpatterns=[
    path('home/', home, name='home'),
    path('analytics/', analytics, name='analytics'),
    path('balance/', balance, name='balance'),
    path('book-form/', add_book, name='add_book'),
    path('shelf/', book_shelf, name='book_shelf'),
    path('book/<int:id>/', book_detail, name='book_detail'),
    path('books/<int:book_id>/edit/', edit_book, name='edit_book'),
    path('authors/', authors_list, name='authors-list'),
    path('authors/<int:author_id>', author_detail, name='authors-detail'),
    path('books/by-genre/', books_by_genre, name='books_by_genre'),



]