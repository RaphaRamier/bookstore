from django.contrib import admin
from .models import Sale


@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
    list_display=(
        'id',
        'book',
        'get_book_edition',
        'get_release_date',
        'sale_date',
        'quantity',
        'total_value'
    )

    list_filter=(
        'book__book__title',
        'book__release_date',
        'book__edition'
    )

    def get_book_edition(self, obj):
        return obj.book.edition

    get_book_edition.admin_order_field='book__edition'
    get_book_edition.short_description='Edition'

    def get_release_date(self, obj):
        return obj.book.release_date

    get_release_date.admin_order_field='book__release_date'
    get_release_date.short_description='Release Date'
