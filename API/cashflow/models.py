from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from API.sales.models import Sale
from API.suppliers.models import Supplier


class CashInFlow(models.Model):
    source=models.ForeignKey(
        Sale,
        on_delete=models.CASCADE,
        related_name='inflow',
        editable=False
    )
    amount=models.DecimalField(
        max_digits=10,
        decimal_places=2,
        editable=False
    )
    date=models.DateTimeField(auto_now_add=True)
    description=models.TextField(
        blank=True,
        null=True
    )

    class Meta:
        ordering=['-date']

    def __str__(self):
        return (f'Source: {self.source}'
                f'Amount: {self.amount}'
                f'Date: {self.date}')


class CashOutFlow(models.Model):
    TYPE_CHOICES=(
        ('SERVICE', 'Service'),
        ('MATERIAL', 'Material'),
    )

    type=models.CharField(
        max_length=10,
        choices=TYPE_CHOICES
    )
    supplier=models.ForeignKey(
        Supplier,
        on_delete=models.PROTECT,
        related_name='outflows'
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

    # Fields for GenericForeignKey
    content_type=models.ForeignKey(ContentType, on_delete=models.PROTECT)
    object_id=models.PositiveIntegerField()
    content_object=GenericForeignKey('content_type', 'object_id')

    class Meta:
        ordering=['-date']

    def __str__(self):
        return (f'Supplier: {self.supplier}'
                f'Type: {self.type}'
                f'Item: {self.content_object}'
                f'Quantity: {self.content_object.quantity if hasattr(self.content_object, "quantity") else "N/A"}'
                f'Amount: {self.amount}'
                f'Date: {self.date}'
                f'Description: {self.description if self.description else "N/A"}')
