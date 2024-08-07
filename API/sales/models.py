import secrets

from django.db import models
from API.buyers.models import Buyer
from API.publication.models import Publication


class Sale(models.Model):
    STATUS_CHOICE = [
        ('SUCCESSFUL', 'Successful'),
        ('PENDING', 'Pending'),
        ('CANCELED', 'Canceled')

    ]

    buyer = models.ForeignKey(
        Buyer,
        on_delete=models.PROTECT,
        related_name='buyers'
    )
    book=models.ForeignKey(
        Publication,
        on_delete=models.PROTECT,
        related_name='sales',
    )
    quantity=models.PositiveIntegerField()
    sale_date=models.DateTimeField(auto_now_add=True)
    total_value=models.DecimalField(max_digits=10, decimal_places=2, editable=False, default=0)
    sale_number=models.CharField(max_length=15, unique=True, blank=True, editable=False)
    status = models.CharField(max_length=10, choices=STATUS_CHOICE, default='PENDING')
    description=models.TextField(editable=False)

    class Meta:
        ordering=['-sale_date']

    def __str__(self):
        return f'{self.book} - {self.quantity}'

    def save(self, *args, **kwargs):
        self.total_value=self.book.price_unit * self.quantity
        if not self.sale_number:
            self.sale_number=self.generate_unique_sale_number()
        self.description=(f'Cash inflow from sale: ',
                          f'ID: {self.id} ',
                          f'Book: {self.book} ',
                          f'Quantity: {self.quantity} ',
                          f'Sale Code: {self.sale_number}',)
        super().save(*args, **kwargs)

    def generate_unique_sale_number(self):
        while True:
            sale_number=''.join([str(secrets.randbelow(10)) for _ in range(15)])
            if not Sale.objects.filter(sale_number=sale_number).exists():
                return sale_number
