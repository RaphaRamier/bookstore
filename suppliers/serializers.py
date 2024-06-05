from rest_framework import serializers
from suppliers.models import Supplier
from suppliers.validators import *


class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model=Supplier
        fields='__all__'
        read_only_fields=('account_number',)

    def validate(self, data):
        if not name_validate(data['name']):
            raise serializers.ValidationError({'nome': 'O nome deve ser válido'})
        if data['person_type'] == 'PF':
            if not cpf_validate(data['document']):
                raise serializers.ValidationError({'cpf': 'Número de CPF inválido'})
        else:
            if not cnpj_validate(data['document']):
                raise serializers.ValidationError({'cnpj': 'Número de CNPJ inválido'})
        if not phone_validate(data['contact_phone']):
            raise serializers.ValidationError(
                {'celular': 'O celular deve seguir este modelo (XX) 9 XXXX-XXXX. (respeitando os espaços e traços)'})

        return data
