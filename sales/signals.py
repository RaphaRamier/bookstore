from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from publication.models import Publication
from sales.models import Sale


@receiver(post_save, sender=Sale)
def update_publication_quantity(sender, instance, **kwargs):
    publication = instance.book
    publication.quantity -= instance.quantity
    publication.save()