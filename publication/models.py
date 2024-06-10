from django.db import models
from assembly.models import BookAssembly
from books.models import Book

STATUS_CHOICES=(
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
    book=models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
        related_name='publications'
    )
    release_date=models.DateField()
    edition=models.CharField(
        max_length=20
    )
    status=models.CharField(
        max_length=20,
        choices=STATUS_CHOICES
    )
    quantity=models.PositiveIntegerField(default=0)
    page_count=models.IntegerField(default=0)
    language=models.CharField(max_length=50)
    assembly=models.ForeignKey(
        BookAssembly,
        on_delete=models.PROTECT,
        related_name='assembly',
        null=True,
        blank=True
    )
    price_unit=models.DecimalField(max_digits=10, decimal_places=2)
    price_total=models.DecimalField(max_digits=10, decimal_places=2, editable=False)

    def __str__(self):
        return f'{self.book.title} - {self.edition}'

    def save(self, *args, **kwargs):
        self.price_total=self.price_unit * self.quantity
        super(Publication, self).save(*args, **kwargs)

