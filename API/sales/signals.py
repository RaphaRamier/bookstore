from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from API.sales.models import Sale
from API.cashflow.models import CashInFlow


@receiver(post_save, sender=Sale)
def update_publication_quantity(sender, instance, **kwargs):
    publication=instance.book
    publication.quantity-=instance.quantity
    publication.save()


@receiver(post_save, sender=Sale)
def create_cash_inflow(sender, instance, created, **kwargs):
    if instance.status == 'SUCCESSFUL':
        if created:
            CashInFlow.objects.create(
                source=instance,
                amount=instance.total_value,
                description=f'Cash inflow from sale: '
                            f'ID: {instance.id} '
                            f'Book: {instance.book} '
                            f'Quantity: {instance.quantity} '
                            f'Status: {instance.status}'
                            f'Sale Code: {instance.sale_number}'
            )
        print('CashInFlow created successfully')


@receiver(post_delete, sender=Sale)
def update_publication_quantity_delete(sender, instance, **kwargs):
    publication=instance.book
    publication.quantity+=instance.quantity
    publication.save()


@receiver(post_delete, sender=Sale)
def handle_sale_deletion(sender, instance, **kwargs):
    cash_inflow_entry=CashInFlow.objects.filter(source=instance).first()
    if cash_inflow_entry:
        cash_inflow_entry.delete()
