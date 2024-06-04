from django.contrib import admin
from books.models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'authors_list',
        'genres_list',
        'synopsis',
        'page_count',
        'language',
        'assembly',
        'isbn',

    )

    list_filter = (
        'title',
        'author',
        'genres',
        'language'
    )
