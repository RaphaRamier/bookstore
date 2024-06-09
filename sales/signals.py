from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from publication.models import Publication
from sales.models import Sale
from cashflow.models import CashInFlow


@receiver(post_save, sender=Sale)
def update_publication_quantity(sender, instance, **kwargs):
    publication = instance.book
    publication.quantity -= instance.quantity
    publication.save()


@receiver(post_save, sender=Sale)
def create_cash_inflow(sender, instance, created, **kwargs):
    if created:
        CashInFlow.objects.create(
            source=instance,
            amount=instance.total_value,
            description=f'Cash inflow from sale: '
                        f'\nID: {instance.id} '
                        f'\nBook: {instance.book} '
                        f'\nQuantity: {instance.quantity} '
                        f'\nSale Code: {instance.sale_number}'
        )
    print('CashOutFlow created successfully')