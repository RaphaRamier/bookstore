from django.contrib import admin
from API.components.models import Component


@admin.register(Component)
class SupplierAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'quantity',
        'price_unit',
        'price_total'
    )

    list_filter = (
        'name',
        'quantity',
        'price_unit',
        'price_total'
    )