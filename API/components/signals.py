from django.contrib.contenttypes.models import ContentType
from django.db.models.signals import post_save
from django.dispatch import receiver
from API.cashflow.models import CashOutFlow
from API.components.models import Component


@receiver(post_save, sender=Component)
def create_cash_outflow_for_component(sender, instance, created, **kwargs):
    if created:
        CashOutFlow.objects.create(
            type='MATERIAL',
            supplier=instance.supplier,
            amount=instance.price_total,
            content_type=ContentType.objects.get_for_model(instance),
            object_id=instance.id,
            description=f'Cash outflow from buy: '
                        f'\nID: {instance.id} '
                        f'\nMaterial: {instance.name} '
                        f'\nQuantity: {instance.quantity}'
        )
    print('CashOutFlow created successfully')