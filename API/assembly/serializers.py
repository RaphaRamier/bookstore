from rest_framework import serializers
from API.assembly.models import BookAssembly


class BookAssemblySerializer(serializers.ModelSerializer):
    class Meta:
        model = BookAssembly
        fields = '__all__'
