from rest_framework import serializers
from API.components.models import Component


class ComponentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Component
        fields='__all__'
        read_only_fields=('amount',)
