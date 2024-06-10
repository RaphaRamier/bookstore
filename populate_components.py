import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')
django.setup()

from faker import Faker
import random
from API.suppliers.models import Supplier
from API.components.models import Component


def criando_componentes(quantidade_de_componentes):
    fake=Faker('pt_BR')
    Faker.seed(10)

    fornecedores=Supplier.objects.all()

    if not fornecedores.exists():
        print("Por favor, crie fornecedores antes de adicionar componentes.")
        return

    for _ in range(quantidade_de_componentes):
        name=fake.word()
        description=fake.text()
        quantity=random.randint(1, 100)
        price_unit=round(random.uniform(1.0, 1000.0), 2)
        supplier=random.choice(fornecedores)
        date=fake.date_between(start_date='-1y', end_date='today')

        component=Component(
            name=name,
            description=description,
            quantity=quantity,
            price_unit=price_unit,
            supplier=supplier,
            date=date
        )
        component.save()



criando_componentes(500)
