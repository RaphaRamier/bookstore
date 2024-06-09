from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from sales.models import Sale
from suppliers.models import Supplier
from components.models import Component


class CashInFlow(models.Model):
    source=models.ForeignKey(
        Sale,
        on_delete=models.PROTECT,
        related_name='inflow',
        editable=False
    )
    amount=models.DecimalField(
        max_digits=10,
        decimal_places=2,
        editable=False
    )
    date=models.DateField(auto_now_add=True)
    description=models.TextField(
        blank=True,
        null=True
    )

    def __str__(self):
        return (f'\nSource: {self.source}'
                f'\nAmount: {self.amount}'
                f'\nDate: {self.date}')


class CashOutFlow(models.Model):
    TYPE_CHOICES = (
        ('SERVICE', 'Service'),
        ('MATERIAL', 'Material'),
    )

    type = models.CharField(
        max_length=10,
        choices=TYPE_CHOICES
    )
    supplier = models.ForeignKey(
        Supplier,
        on_delete=models.PROTECT,
        related_name='outflows'
    )
    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        editable=False
    )
    date = models.DateField(auto_now_add=True)
    description = models.TextField(
        blank=True,
        null=True
    )

    # Fields for GenericForeignKey
    content_type = models.ForeignKey(ContentType, on_delete=models.PROTECT)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return (f'Supplier: {self.supplier}\n'
                f'Type: {self.type}\n'
                f'Item: {self.content_object}\n'
                f'Quantity: {self.content_object.quantity if hasattr(self.content_object, "quantity") else "N/A"}\n'
                f'Amount: {self.amount}\n'
                f'Date: {self.date}\n'
                f'Description: {self.description if self.description else "N/A"}')