import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')
django.setup()

import random
from faker import Faker
from datetime import timedelta
from API.buyers.models import Buyer
from API.publication.models import Publication
from API.sales.models import Sale

fake=Faker('pt_BR')
Faker.seed(42)


def criar_vendas(quantidade_de_vendas):
    buyers=Buyer.objects.all()
    books=Publication.objects.all()

    if not buyers.exists() or not books.exists():
        print("Por favor, crie compradores e publicações antes de adicionar vendas.")
        return

    for _ in range(quantidade_de_vendas):
        buyer=random.choice(buyers)
        book=random.choice(books)
        quantity=random.randint(1, 30)
        sale_date=fake.date_between(start_date='-3y', end_date='today')
        status=random.choice(['SUCCESSFUL', 'PENDING', 'CANCELED'])

        sale=Sale(
            buyer=buyer,
            book=book,
            quantity=quantity,
            sale_date=sale_date,
            status=status
        )
        sale.save()

        print(f"Criada venda: {sale}")


criar_vendas(500)
