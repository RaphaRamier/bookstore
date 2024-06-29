from django.urls import path
from Client.client.views import home, analytics, balance, add_book, book_shelf, book_detail, edit_book

urlpatterns=[
    path('home/', home, name='home'),
    path('analytics/', analytics, name='analytics'),
    path('balance/', balance, name='balance'),
    path('book-form/', add_book, name='add_book'),
    path('shelf/', book_shelf, name='book_shelf'),
    path('book/<int:id>/', book_detail, name='book_detail'),
    path('books/<int:book_id>/edit/', edit_book, name='edit_book'),

]