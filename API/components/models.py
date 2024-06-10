from django.db import models
from API.suppliers.models import Supplier


class Component(models.Model):
    name=models.CharField(max_length=255)
    description=models.TextField()
    quantity = models.IntegerField()
    price_unit=models.DecimalField(max_digits=10, decimal_places=2)
    price_total=models.DecimalField(max_digits=10, decimal_places=2, editable=False)
    supplier=models.ForeignKey(Supplier, on_delete=models.CASCADE, related_name='components')
    date = models.DateField()

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.price_total=self.price_unit * self.quantity
        super(Component, self).save(*args, **kwargs)
