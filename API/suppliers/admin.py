from django.contrib import admin
from API.suppliers.models import Supplier


@admin.register(Supplier)
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


