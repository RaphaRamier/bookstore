from django.db import models
from API.authors.models import Authors
from API.genres.models import Genre


class Book(models.Model):
    title=models.CharField(max_length=500)
    author=models.ManyToManyField(
        Authors,
        related_name='author'
    )
    isbn=models.CharField(
        max_length=13,
        unique=True)
    genres=models.ManyToManyField(
        Genre,
        related_name='genre'
    )
    synopsis=models.TextField(
        null=True,
        blank=True
    )

    def __str__(self):
        return self.title
