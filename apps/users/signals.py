from django.db.models.signals import post_save
from apps.profiles.models import Profile
from apps.agents.models import Agent
# from apps.organizations.models import Organization
from django.dispatch import receiver


# --------------------------------------------------------



# --------------------------------------------------------
# Auto add Agent
@receiver(post_save, sender=Profile)
def create_profile_agentid(sender, instance, created, **kwargs):
    if created:
        Agent.objects.create(profile=instance)


@receiver(post_save, sender=Profile)
def save_profile_agentid(sender, instance, **kwargs):
    instance.agent.save()

# --------------------------------------------------------
# # Auto add company
# @receiver(post_save, sender=Profile)
# def create_profile_organization(sender, instance, created, **kwargs):
#     if created:
#         Organization.objects.create(profile=instance)


# @receiver(post_save, sender=Profile)
# def save_profile_agentid(sender, instance, **kwargs):
#     instance.organization.save()
