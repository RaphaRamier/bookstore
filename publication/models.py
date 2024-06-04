from django.db import models
from books.models import Book

STATUS_CHOICES = (
    ('published', 'Published'),
    ('out_of_circulation', 'Out of Circulation'),
    ('in_printing', 'In Printing'),
    ('in_test_layout', 'In Test Layout'),
    ('in_test_ink', 'In Test Ink'),
    ('in_review', 'In Review'),
    ('all_sold', 'All Sold'),
    ('pre_sale', 'Pre-Sale'),

)


class Publication(models.Model):
    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
        related_name='publications'
    )
    release_date = models.DateField()
    edition = models.CharField(
        max_length=20
    )
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES
    )
    quantity = models.IntegerField()

    def __str__(self):
        return f'{self.book.title} - {self.edition}'