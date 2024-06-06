import os
import django
from random import choice, randint
from datetime import datetime, timedelta
from faker import Faker

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')
django.setup()

from books.models import Book
from assembly.models import BookAssembly
from publication.models import Publication

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

        publicacao=Publication(
            book=livro,
            release_date=data_de_lancamento,
            edition=edicao,
            status=status,
            quantity=quantidade,
            page_count=contagem_de_paginas,
            language=idioma,
            assembly=assembly
        )
        publicacao.save()
        print(f'Publicação criada: {publicacao.book.title} - {publicacao.edition}')



criar_publicacoes()
