import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')
django.setup()

from faker import Faker
from validate_docbr import CPF, CNPJ
import random
from API.suppliers.models import Supplier


def criando_fornecedores(quantidade_de_fornecedores):
    fake=Faker('pt_BR')
    Faker.seed(10)
    for _ in range(quantidade_de_fornecedores):
        person_type=random.choice(['PF', 'PJ'])
        if person_type == 'PF':
            document=CPF().generate()
        else:
            document=CNPJ().generate()

        name=fake.company() if person_type == 'PJ' else fake.name()
        contact_name=fake.name()
        contact_email='{}@{}'.format(contact_name.lower().replace(' ', ''), fake.free_email_domain())
        contact_phone="{} 9{}-{}".format(random.randrange(10, 21), random.randrange(4000, 9999),
                                         random.randrange(4000, 9999))
        address=fake.address()

        supplier=Supplier(
            person_type=person_type,
            name=name,
            contact_name=contact_name,
            contact_email=contact_email,
            contact_phone=contact_phone,
            address=address,
            document=document
        )
        supplier.save()


criando_fornecedores(50)
