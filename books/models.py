from django.db import models
from authors.models import Authors
from genres.models import Genre
from assembly.models import BookAssembly


class Book(models.Model):
    title = models.CharField(max_length=500)
    author = models.ManyToManyField(
        Authors,
        related_name='author'
    )
    isbn = models.CharField(
        max_length=13,
        unique=True)
    genres = models.ManyToManyField(
        Genre,
        related_name='genre'
    )
    synopsis = models.TextField(
        null=True,
        blank=True
    )
    page_count = models.IntegerField(default=0)
    language = models.CharField(max_length=50)
    assembly = models.ForeignKey(
        BookAssembly,
        on_delete=models.PROTECT,
        related_name='assembly',
        null=True,
        blank=True
    )

    def __str__(self):
        return self.title

    def genres_list(self):
        return ", ".join([genre.name for genre in self.genres.all()])

    genres_list.short_description = 'Genres'

    def authors_list(self):
        return ", ".join([author.name for author in self.author.all()])

    authors_list.short_description = 'Authors'
