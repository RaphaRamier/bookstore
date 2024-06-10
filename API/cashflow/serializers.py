from rest_framework import serializers
from .models import CashInFlow, CashOutFlow


class CashInFlowSerializer(serializers.ModelSerializer):
    class Meta:
        model=CashInFlow
        fields='__all__'
        read_only_fields=('price_total', 'source')


class CashOutFlowSerializer(serializers.ModelSerializer):
    class Meta:
        model=CashOutFlow
        fields='__all__'
        read_only_fields=('type',
                          'supplier',
                          'amount')
