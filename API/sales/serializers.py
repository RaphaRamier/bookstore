from rest_framework import serializers
from API.publication.models import Publication
from API.sales.models import Sale


class SaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sale
        fields = '__all__'

    def validate_quantity(self, value):
        instance = self.instance
        if instance:
            available_quantity = instance.book.quantity + instance.quantity
        else:
            book_id = self.initial_data.get('book')
            if not book_id:
                return value
            try:
                book = Publication.objects.get(pk=book_id)
            except Publication.DoesNotExist:
                return value
            available_quantity = book.quantity
        if value > available_quantity:
            raise serializers.ValidationError("A quantidade vendida não pode ser maior do que a quantidade disponível.")
        return value