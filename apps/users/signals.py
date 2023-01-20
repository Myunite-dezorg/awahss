from django.db.models.signals import post_save
from apps.profiles.models import Profile
from apps.agents.models import Agent
# from apps.organizations.models import Organization
from django.dispatch import receiver


# Auto add Agent
@receiver(post_save, sender=Profile)
def create_profile_agentid(sender, instance, created, **kwargs):
    if created:
        Agent.objects.create(profile=instance)

# @receiver(post_save, sender=User)
# def post_save_user_signal_handler(sender, instance, created, **kwargs):
#     if created:
#        instance.is_active = True
#        instance.is_staff = True
#        group = Group.objects.get(name='Registered users')
#        instance.groups.add(group)

@receiver(post_save, sender=Profile)
def save_profile_agentid(sender, instance, **kwargs):
    instance.agent.save()