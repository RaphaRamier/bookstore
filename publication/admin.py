from django.contrib import admin
from publication.models import Publication


@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'book',
        'edition',
        'release_date',
        'price_unit',
        'price_total'
    )

    list_filter = (
        'status',
        'language'
    )

    search_fields = (
        'book__title',
        'edition',

    )