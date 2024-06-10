import os
import django
from random import choice, uniform
from decimal import Decimal

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')
django.setup()

from API.assembly.models import BookAssembly


def criando_book_assemblies(quantidade_de_assemblies):
    PAPER_CHOICES=['glossy', 'matte', 'recycled', 'bond']
    COVER_CHOICES=['hardcover', 'paperback', 'spiral']
    BINDING_CHOICES=['perfect', 'saddle', 'case', 'spiral']

    for _ in range(quantidade_de_assemblies):
        binding_type=choice(BINDING_CHOICES)
        paper_type=choice(PAPER_CHOICES)
        cover_type=choice(COVER_CHOICES)
        weight=round(uniform(0.1, 3.0), 2)  # Garante que o peso esteja entre 0.1 e 3.0 kg

        try:
            book_assembly=BookAssembly(
                binding_type=binding_type,
                paper_type=paper_type,
                cover_type=cover_type,
                weight=Decimal(weight)
            )
            book_assembly.save()
            print(f'BookAssembly created: {book_assembly}')
        except Exception as e:
            print(f'Error creating BookAssembly: {e}')


criando_book_assemblies(50)
