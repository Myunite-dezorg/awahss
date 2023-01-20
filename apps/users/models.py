from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager
from django.db.models.signals import post_save
from django.contrib.auth.models import Group
from django.dispatch import receiver


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    # is_agent = models.BooleanField(default=False)
    # is_manager = models.BooleanField(default=False)
    # is_accounter = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)


    # following = models.ManyToManyField("self", blank=True, related_name="followers", symmetrical=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

# class Manager(User):
#     is_manager = models.BooleanField(default=True)


#     def __str__(self):
#         return self.email

class Partner(User):
    is_agent = models.BooleanField(default=True)

    def __str__(self):
        return self.email



# class Accounting(User):
#     is_accounter = models.BooleanField(default=True)

#     def __str__(self):
#         return self.email



