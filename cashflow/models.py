from django.db import models
from sales.models import Sale
from suppliers.models import Supplier
from components.models import Component


class CashInFlow(models.Model):
    source=models.ForeignKey(
        Sale,
        on_delete=models.PROTECT,
        related_name='inflow'
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
    TYPE_CHOICE=(
        ('SERVICE', 'Service'),
        ('MATERIAL', 'Material')
    )

    type=models.CharField(
        max_length=10,
        choices=TYPE_CHOICE
    )
    supplier=models.ForeignKey(
        Supplier,
        on_delete=models.PROTECT,
        related_name='outflow'
    )
    material=models.ForeignKey(
        Component,
        on_delete=models.PROTECT,
        related_name='material'
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
        return (f'\nSupplier: {self.supplier}'
                f'\nMaterial: {self.material}'
                f'\nQuantity: {self.material.quantity}'
                f'\nAmount: {self.amount}'
                )
