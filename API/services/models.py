from django.db import models
from API.suppliers.models import Supplier


class Service(models.Model):
    SERVICE_TYPE_CHOICES=[
        ('RECURRING', 'Recurring'),
        ('SPECIFIC', 'Specific'),
    ]

    name=models.CharField(max_length=255)
    description=models.TextField()
    service_type=models.CharField(max_length=20, choices=SERVICE_TYPE_CHOICES)
    price_total=models.DecimalField(max_digits=10, decimal_places=2)
    supplier=models.ForeignKey(Supplier, on_delete=models.CASCADE, related_name='services')
    date=models.DateField()

    def __str__(self):
        return f'{self.name} - {self.supplier} - {self.price_total}'
