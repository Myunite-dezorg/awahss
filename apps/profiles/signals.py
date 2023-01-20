from apps.users.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.profiles.models import Profile

#------User profile created------

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

# #------Accounter profile created------

# @receiver(post_save, sender=Accounting)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(accounting=instance)

# @receiver(post_save, sender=Accounting)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()


# #------Manager profile created------

# @receiver(post_save, sender=Manager)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(manager=instance)

# @receiver(post_save, sender=Manager)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()


# #------Partner profile created------

# @receiver(post_save, sender=Partner)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(partner=instance)

# @receiver(post_save, sender=Partner)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()
