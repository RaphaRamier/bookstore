from django.contrib import admin
from publication.models import Publication


@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'book',
        'edition',
        'release_date'
    )

    list_filter = (
        'book',
        'release_date',
        'edition'
    )