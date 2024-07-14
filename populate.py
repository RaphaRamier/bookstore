from datetime import timedelta, datetime
from decimal import Decimal
import django
import os
import sys



# Configurar o ambiente Django
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
os.environ['DJANGO_SETTINGS_MODULE'] = 'setup.settings'
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "setup.settings")
django.setup()

from validate_docbr import CPF, CNPJ
from API.assembly.models import BookAssembly
from API.components.models import Component
from API.books.models import Book
from API.buyers.models import Buyer
from API.genres.models import Genre
from API.publication.models import Publication
from API.sales.models import Sale
from API.suppliers.models import Supplier
from faker import Faker
from API.authors.models import Authors, NATIONALITY_CHOICES
import random

fake = Faker()

def criar_generos():
    try:
        generos_comuns = [
            "Ficção Científica", "Fantasia", "Romance", "Mistério",
            "Terror", "Aventura", "Biografia", "História",
            "Autoajuda", "Poesia"
        ]

        for genero in generos_comuns:
            genre, created = Genre.objects.get_or_create(name=genero)
            if created:
                print(f"Gênero '{genero}' criado com sucesso.")
            else:
                print(f"Gênero '{genero}' já existe.")

        print("Gêneros populados com sucesso.")
    except Exception as e:
        print(f"Erro ao criar gêneros: {e}")

def criando_autores(quantidade_de_autores):
    try:
        nacionalidades = [choice[0] for choice in NATIONALITY_CHOICES]

        for _ in range(quantidade_de_autores):
            name = fake.name()
            biography = fake.text()
            birthday = fake.date_of_birth(tzinfo=None, minimum_age=25, maximum_age=85)
            nationality = random.choice(nacionalidades)

            autor = Authors(
                name=name,
                biography=biography,
                birthday=birthday,
                nationality=nationality
            )
            autor.save()
    except Exception as e:
        print(f"Erro ao criar autores: {e}")

def criando_book_assemblies(quantidade_de_assemblies):
    try:
        PAPER_CHOICES = ['glossy', 'matte', 'recycled', 'bond']
        COVER_CHOICES = ['hardcover', 'paperback', 'spiral']
        BINDING_CHOICES = ['perfect', 'saddle', 'case', 'spiral']

        for _ in range(quantidade_de_assemblies):
            binding_type = random.choice(BINDING_CHOICES)
            paper_type = random.choice(PAPER_CHOICES)
            cover_type = random.choice(COVER_CHOICES)
            weight = round(random.uniform(0.1, 3.0), 2)

            book_assembly = BookAssembly(
                binding_type=binding_type,
                paper_type=paper_type,
                cover_type=cover_type,
                weight=Decimal(weight)
            )
            book_assembly.save()
            print(f'BookAssembly created: {book_assembly}')
    except Exception as e:
        print(f"Erro ao criar book assemblies: {e}")

def criando_compradores(quantidade_de_compradores):
    try:
        for _ in range(quantidade_de_compradores):
            person_type = random.choice(['PF', 'PJ'])
            document = CPF().generate() if person_type == 'PF' else CNPJ().generate()
            name = fake.company() if person_type == 'PJ' else fake.name()
            contact_name = fake.name()
            contact_email = '{}@{}'.format(contact_name.lower().replace(' ', ''), fake.free_email_domain())
            contact_phone = "{} 9{}-{}".format(random.randrange(10, 21), random.randrange(4000, 9999), random.randrange(4000, 9999))
            address = fake.address()

            data = Buyer(
                person_type=person_type,
                name=name,
                contact_name=contact_name,
                contact_email=contact_email,
                contact_phone=contact_phone,
                address=address,
                document=document
            )
            data.save()
    except Exception as e:
        print(f"Erro ao criar compradores: {e}")

def criando_fornecedores(quantidade_de_fornecedores):
    try:
        for _ in range(quantidade_de_fornecedores):
            person_type = random.choice(['PF', 'PJ'])
            document = CPF().generate() if person_type == 'PF' else CNPJ().generate()
            name = fake.company() if person_type == 'PJ' else fake.name()
            contact_name = fake.name()
            contact_email = '{}@{}'.format(contact_name.lower().replace(' ', ''), fake.free_email_domain())
            contact_phone = "{} 9{}-{}".format(random.randrange(10, 21), random.randrange(4000, 9999), random.randrange(4000, 9999))
            address = fake.address()

            supplier = Supplier(
                person_type=person_type,
                name=name,
                contact_name=contact_name,
                contact_email=contact_email,
                contact_phone=contact_phone,
                address=address,
                document=document
            )
            supplier.save()
    except Exception as e:
        print(f"Erro ao criar fornecedores: {e}")

def gerar_isbn_unico():
    while True:
        isbn = fake.isbn13(separator="")
        if not Book.objects.filter(isbn=isbn).exists():
            return isbn

def criando_livros(quantidade_de_livros):
    try:
        generos_existentes = list(Genre.objects.all())
        autores_existentes = list(Authors.objects.all())

        if not generos_existentes or not autores_existentes:
            print("Não há gêneros ou autores suficientes no banco de dados.")
            return

        for _ in range(quantidade_de_livros):
            titulo = fake.sentence(nb_words=4)
            isbn = gerar_isbn_unico()
            sinopse = fake.text(max_nb_chars=200)
            livro = Book(
                title=titulo,
                isbn=isbn,
                synopsis=sinopse
            )
            livro.save()

            num_generos = random.randint(1, 3)
            num_autores = random.randint(1, 3)
            livro.genres.set(random.choice(generos_existentes) for _ in range(num_generos))
            livro.author.set(random.choice(autores_existentes) for _ in range(num_autores))

            livro.save()
            print(f'Book created: {livro.title} - ISBN: {livro.isbn}')
    except Exception as e:
        print(f"Erro ao criar livros: {e}")

def criando_componentes(quantidade_de_componentes):
    try:
        fornecedores = Supplier.objects.all()

        if not fornecedores.exists():
            print("Por favor, crie fornecedores antes de adicionar componentes.")
            return

        for _ in range(quantidade_de_componentes):
            name = fake.word()
            description = fake.text()
            quantity = random.randint(1, 100)
            price_unit = round(random.uniform(1.0, 1000.0), 2)
            supplier = random.choice(fornecedores)
            date = fake.date_between(start_date='-1y', end_date='today')

            component = Component(
                name=name,
                description=description,
                quantity=quantity,
                price_unit=price_unit,
                supplier=supplier,
                date=date
            )
            component.save()
    except Exception as e:
        print(f"Erro ao criar componentes: {e}")

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
        assembly= random.choice(assemblies_existentes) if assemblies_existentes else None
        data_de_lancamento=fake.date_between(start_date='-2y', end_date='today')
        edicao=f'{random.randint(1, 10)}ª Edição'
        status= random.choice(STATUS_CHOICES)
        quantidade= random.randint(100, 5000)
        contagem_de_paginas= random.randint(50, 1000)
        idioma= random.choice(LANGUAGE_CHOICES)
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





def criar_vendas():
    try:
        buyers = Buyer.objects.all()
        publications = Publication.objects.all()

        if not buyers.exists() or not publications.exists():
            print("Por favor, crie compradores e publicações antes de adicionar vendas.")
            return

        start_date = datetime.now() - timedelta(days=809)  # 3 anos atrás
        end_date = datetime.now()

        current_date = start_date

        while current_date <= end_date:
            genres = list(publications.values_list('book__genres__name', flat=True).distinct())

            for genre in genres:
                status = random.choice(['SUCCESSFUL', 'PENDING', 'CANCELED'])
                quantity = random.randint(1, 10)

                publication = random.choice(publications.filter(book__genres__name=genre))
                sale_date = current_date.replace(hour=0, minute=0, second=0, microsecond=0)

                sale = Sale(
                    buyer=random.choice(buyers),
                    book=publication,
                    quantity=quantity,
                    sale_date=sale_date,
                    status=status
                )
                sale.save()

                print(f"Venda criada para o dia {current_date}: {sale}")

            current_date += timedelta(days=1)

        print("Vendas criadas com sucesso.")
    except Exception as e:
        print(f"Erro ao criar vendas: {e}")

# Executar todas as funções de criação
criar_generos()
criando_autores(50)
criando_book_assemblies(50)
criando_compradores(50)
criando_fornecedores(50)
criando_livros(50)
criar_publicacoes()
criando_componentes(50)
criar_vendas()
