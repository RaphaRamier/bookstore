from django.contrib.contenttypes.models import ContentType
from django.db.models.signals import post_save
from django.dispatch import receiver
from cashflow.models import CashOutFlow
from services.models import Service

@receiver(post_save, sender=Service)
def create_cash_outflow_for_service(sender, instance, created, **kwargs):
    if created:
        CashOutFlow.objects.create(
            type='SERVICE',
            supplier=instance.supplier,
            amount=instance.price_total,
            content_type=ContentType.objects.get_for_model(instance),
            object_id=instance.id,
            description=f'Cash outflow from Service: '
                        f'\nID: {instance.id} '
                        f'\nService Type: {instance.service_type} '
                        f'\nService Name: {instance.name} '
        )