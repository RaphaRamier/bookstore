from django.contrib import admin
from API.buyers.models import Buyer


@admin.register(Buyer)
class SupplierAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'document',
        'person_type'
    )

    list_filter = (
        'name',
        'person_type'
    )

