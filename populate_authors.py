import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')
django.setup()

from faker import Faker
from authors.models import Authors, NATIONALITY_CHOICES
import random


def criando_autores(quantidade_de_autores):
    fake=Faker()
    Faker.seed(10)

    nacionalidades=[choice[0] for choice in NATIONALITY_CHOICES]

    for _ in range(quantidade_de_autores):
        name=fake.name()
        biography=fake.text()
        birthday=fake.date_of_birth(tzinfo=None, minimum_age=25, maximum_age=85)
        nationality=random.choice(nacionalidades)

        autor=Authors(
            name=name,
            biography=biography,
            birthday=birthday,
            nationality=nationality
        )
        autor.save()


criando_autores(50)
