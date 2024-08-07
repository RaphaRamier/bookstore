import os
import django
from random import choice, randint
from faker import Faker

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')
django.setup()

from API.books import Book
from API.assembly.models import BookAssembly
from API.publication import Publication

fake=Faker()

STATUS_CHOICES=[
    'published', 'out_of_circulation', 'in_printing', 'in_test_layout',
    'in_test_ink', 'in_review', 'all_sold', 'pre_sale'
]

LANGUAGE_CHOICES=[
    'English', 'Portuguese', 'Spanish', 'French', 'German', 'Italian', 'Chinese', 'Japanese', 'Korean', 'Russian'
]


def criar_publicacoes():
    livros_sem_publicacao=Book.objects.filter(publications__isnull=True)
    assemblies_existentes=list(BookAssembly.objects.all())

    if not livros_sem_publicacao:
        print("Todos os livros existentes já possuem pelo menos uma publicação associada.")
        return

    for livro in livros_sem_publicacao:
        assembly=choice(assemblies_existentes) if assemblies_existentes else None
        data_de_lancamento=fake.date_between(start_date='-2y', end_date='today')
        edicao=f'{randint(1, 10)}ª Edição'
        status=choice(STATUS_CHOICES)
        quantidade=randint(100, 5000)
        contagem_de_paginas=randint(50, 1000)
        idioma=choice(LANGUAGE_CHOICES)
        price_unit=round(random.uniform(1.0, 1000.0), 2)

        publicacao=Publication(
            book=livro,
            release_date=data_de_lancamento,
            edition=edicao,
            status=status,
            quantity=quantidade,
            page_count=contagem_de_paginas,
            language=idioma,
            assembly=assembly,
            price_unit=price_unit
        )
        publicacao.save()
        print(f'Publicação criada: {publicacao.book.title} - {publicacao.edition}')



criar_publicacoes()
