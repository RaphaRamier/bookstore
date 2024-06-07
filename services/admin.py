from django.contrib import admin
from services.models import Service


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'service_type',
        'price_total',
        'date'

    )

    list_filter = (
        'name',
        'service_type'
    )


