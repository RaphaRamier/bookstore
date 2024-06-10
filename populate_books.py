import os
import django
from random import choice, randint
from faker import Faker

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')
django.setup()

from API.books import Book
from API.authors import Authors
from API.genres.models import Genre

fake=Faker()


def gerar_isbn_unico():
    while True:
        isbn=fake.isbn13(separator="")
        if not Book.objects.filter(isbn=isbn).exists():
            return isbn


def criando_livros(quantidade_de_livros):
    generos_existentes=list(Genre.objects.all())
    autores_existentes=list(Authors.objects.all())

    if not generos_existentes or not autores_existentes:
        print("Não há gêneros ou autores suficientes no banco de dados.")
        return

    for _ in range(quantidade_de_livros):
        titulo=fake.sentence(nb_words=4)
        isbn=gerar_isbn_unico()
        sinopse=fake.text(max_nb_chars=200)
        livro=Book(
            title=titulo,
            isbn=isbn,
            synopsis=sinopse
        )
        livro.save()

        # Adicionando gêneros e autores ao livro
        num_generos=randint(1, 3)
        num_autores=randint(1, 3)
        livro.genres.set(choice(generos_existentes) for _ in range(num_generos))
        livro.author.set(choice(autores_existentes) for _ in range(num_autores))

        livro.save()
        print(f'Book created: {livro.title} - ISBN: {livro.isbn}')


# Criar 50 livros
criando_livros(50)
