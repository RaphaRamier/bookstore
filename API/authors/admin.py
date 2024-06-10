from django.contrib import admin
from API.authors.models import Authors


@admin.register(Authors)
class AuthorAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'birthday',
        'biography',
        'nationality'
    )

    list_filter = (
        'name',
        'nationality'
    )
