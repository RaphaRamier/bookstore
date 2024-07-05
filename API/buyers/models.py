import secrets

from django.db import models

class Buyer(models.Model):
    PERSON_CHOICES=(
        ('PF', 'Pessoa Física'),
        ('PJ', 'Pessoa Jurídica'),
    )
    person_type=models.CharField(max_length=2, choices=PERSON_CHOICES)
    name=models.CharField(max_length=255)
    contact_name=models.CharField(max_length=255)
    contact_email=models.EmailField()
    contact_phone=models.CharField(max_length=20, null=True, blank=True)
    address=models.TextField()
    document=models.CharField(max_length=14, unique=True)
    account_number=models.CharField(max_length=10, unique=True, blank=True, editable=False)

    def save(self, *args, **kwargs):
        if not self.account_number:
            self.account_number=self.generate_unique_account_number()
        super(Buyer, self).save(*args, **kwargs)

    def generate_unique_account_number(self):
        while True:
            account_number=''.join([str(secrets.randbelow(10)) for _ in range(10)])
            if not Buyer.objects.filter(account_number=account_number).exists():
                return account_number

    def __str__(self):
        return self.name