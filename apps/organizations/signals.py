from apps.users.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Organization

# @receiver(post_save, sender=User)
# def create_user_profile_company(sender, instance, created, **kwargs):
#     if created:
#         Organization.objects.create(user=instance)

# @receiver(post_save, sender=User)
# def save_user_profile_company(sender, instance, **kwargs):
#     instance.organization.save()
