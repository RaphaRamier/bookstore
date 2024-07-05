import os
import django
import random
from decimal import Decimal

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')
django.setup()

from API.publication.models import Publication


def populate_prices():
    publications=Publication.objects.all()
    for pub in publications:
        if pub.price_unit == 0:
            price_unit=Decimal(random.uniform(10, 100)).quantize(Decimal('0.01'))
            pub.price_unit=price_unit
            pub.save()
            print(f"Preço adicionado para a publicação: {pub}")


if __name__ == '__main__':
    populate_prices()
