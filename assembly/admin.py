from django.contrib import admin
from assembly.models import BookAssembly


@admin.register(BookAssembly)
class BookAssemblyAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'binding_type',
        'paper_type',
        'cover_type',
        'page_count',
        'weight'
    )

    list_filter = (
        'binding_type',
        'paper_type',
        'cover_type',
    )
