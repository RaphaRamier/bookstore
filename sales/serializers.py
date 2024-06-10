from rest_framework import serializers

from publication.models import Publication
from sales.models import Sale


class SaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sale
        fields = '__all__'

    def validate_quantity(self, value):
        instance = self.instance
        if instance:
            available_quantity = instance.book.quantity + instance.quantity
        else:
            # Obtém o ID do livro do initial_data
            book_id = self.initial_data.get('book')
            if not book_id:
                return value  # Se não houver ID de livro, não podemos validar a quantidade
            try:
                # Obtém o objeto de modelo Publication com base no ID fornecido
                book = Publication.objects.get(pk=book_id)
            except Publication.DoesNotExist:
                return value  # Se o livro não existir, não podemos validar a quantidade
            available_quantity = book.quantity
        if value > available_quantity:
            raise serializers.ValidationError("A quantidade vendida não pode ser maior do que a quantidade disponível.")
        return value