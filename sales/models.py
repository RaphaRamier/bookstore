from django.db import models
from publication.models import Publication


class Sale(models.Model):
    book = models.ForeignKey(
        Publication,
        on_delete=models.PROTECT,
        related_name='sales'
    )
    quantity = models.PositiveIntegerField()
    first_sale = models.DateTimeField(auto_now_add=True)
    last_sale = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-last_sale']

    def __str__(self):
        return f'{self.book.title} - {self.book.edition} - {self.quantity}'
