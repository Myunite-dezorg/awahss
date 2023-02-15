from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import AogService
from apps.orders.models.aog_service_order import AogOrder

@receiver(post_save, sender=AogService)
def create_order(sender, instance, created, **kwargs):
    if created:
        AogOrder.objects.create(service_request=instance)

post_save.connect(create_order, sender=AogService)