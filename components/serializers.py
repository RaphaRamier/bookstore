from rest_framework import serializers
from components.models import Component


class ComponentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Component
        fields='__all__'
        read_only_fields=('amount',)
