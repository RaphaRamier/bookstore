import os
import django
import random
from faker import Faker
from datetime import timedelta, datetime

# Configurar as configurações do Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')
django.setup()

# Importar modelos do Django após a configuração
from API.buyers.models import Buyer
from API.publication.models import Publication
from API.sales.models import Sale

fake=Faker('pt_BR')
Faker.seed(42)


def criar_vendas():
    buyers=Buyer.objects.all()
    publications=Publication.objects.all()

    if not buyers.exists() or not publications.exists():
        print("Por favor, crie compradores e publicações antes de adicionar vendas.")
        return

    # Definir datas de início e fim para as vendas
    start_date=datetime.now() - timedelta(days=809)  # 3 anos atrás
    end_date=datetime.now()

    current_date=start_date

    while current_date <= end_date:
        genres=list(publications.values_list('book__genres__name', flat=True).distinct())

        for genre in genres:
            status=random.choice(['SUCCESSFUL', 'PENDING', 'CANCELED'])
            quantity=random.randint(1, 10)  # Quantidade mais linear

            # Escolher aleatoriamente um livro dentro do gênero especificado
            publication=random.choice(publications.filter(book__genres__name=genre))

            sale_date=current_date.replace(hour=0, minute=0, second=0, microsecond=0)

            sale=Sale(
                buyer=random.choice(buyers),
                book=publication,
                quantity=quantity,
                sale_date=sale_date,
                status=status
            )
            sale.save()

            print(f"Venda criada para o dia {current_date}: {sale}")

        current_date+=timedelta(days=1)

    print("Vendas criadas com sucesso.")


if __name__ == "__main__":
    criar_vendas()
