from django.contrib import admin
from API.assembly.models import BookAssembly


@admin.register(BookAssembly)
class BookAssemblyAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'binding_type',
        'paper_type',
        'cover_type',
        'weight'
    )

    list_filter = (
        'binding_type',
        'paper_type',
        'cover_type',
    )
