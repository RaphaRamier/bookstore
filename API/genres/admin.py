from django.contrib import admin
from API.genres.models import Genre


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name'
    )

    list_filter = (
        'name',
    )
