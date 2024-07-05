from django.contrib import admin

from .models import Sale


@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
    list_display=(
        'id',
        'book',
        'get_book_edition',
        'get_release_date',
        'buyer',
        'sale_date',
        'quantity',
        'total_value',
        'get_quantity_in_stock'

    )

    list_filter=(
        'book__book__title',
        'book__release_date',
        'book__edition',
        'buyer'
    )

    search_fields=(
        'book',
        'sale_date',
        'buyer'
    )

    def get_book_edition(self, obj):
        return obj.book.edition

    get_book_edition.admin_order_field='book__edition'
    get_book_edition.short_description='Edition'

    def get_release_date(self, obj):
        return obj.book.release_date

    def get_quantity_in_stock(self, obj):
        try:
            publication=obj.book
            if publication:
                return publication.quantity
        except AttributeError:
            pass
        return 0

    get_quantity_in_stock.admin_order_field='book__publications__quantity'
    get_quantity_in_stock.short_description='In Stock'

    get_release_date.admin_order_field='book__release_date'
    get_release_date.short_description='Release Date'
