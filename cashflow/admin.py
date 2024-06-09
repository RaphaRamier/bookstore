from django.contrib import admin
from cashflow.models import CashInFlow, CashOutFlow


@admin.register(CashInFlow)
class CashInFlowAdmin(admin.ModelAdmin):
    list_display=(
        'id',
        'source',
        'description',
        'amount',
        'date'
    )

    list_filter=(
        'source',
        'date'
    )
    search_fields=(
        'source__id',
        'source__sale_number'
    )


@admin.register(CashOutFlow)
class CashOutFlowAdmin(admin.ModelAdmin):
    list_display=(
        'id',
        'supplier',
        'type',
        'get_content_object',
        'description',
        'amount',
        'date'
    )

    list_filter=(
        'supplier',
        'date',
        'type'
    )

    search_fields=(
        'supplier__id',
        'supplier__name',
    )

    def get_content_object(self, obj):
        return str(obj.content_object)

    get_content_object.short_description='Item'
