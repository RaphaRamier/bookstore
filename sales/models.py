from django.db import models
from publication.models import Publication


class Sale(models.Model):
    book=models.ForeignKey(
        Publication,
        on_delete=models.PROTECT,
        related_name='sales'
    )
    quantity=models.PositiveIntegerField()
    sale_date=models.DateTimeField(auto_now_add=True)
    total_value=models.DecimalField(max_digits=10, decimal_places=2, editable=False, default=0)

    class Meta:
        ordering=['-sale_date']

    def __str__(self):
        return f'{self.book} - {self.quantity}'

    def save(self, *args, **kwargs):
        self.total_value=self.book.price_unit * self.quantity
        super().save(*args, **kwargs)
