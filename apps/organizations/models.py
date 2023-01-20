from django.db import models
from apps.users.models import User
from apps.profiles.models import Profile
from django.utils.translation import gettext_lazy as _
from apps.organizations.uuid import BaseUUID


class Organization(BaseUUID):


    class Meta:
        ordering = ["name"]
        verbose_name = _("Company")
        verbose_name_plural = _("Companies")
   
    user = models.OneToOneField(User,  on_delete=models.CASCADE)
    # user = models.OneToOneField(User, on_delete=models.PROTECT)
    name = models.CharField(
        _("Name"), max_length=50, default="Person Company LTD")
    email = models.EmailField(_("Email"), blank=True, null=True)
    website = models.URLField(_("Website"), blank=True, null=True)
    phone = models.CharField(_("Phone"), max_length=40, null=True, blank=True)
    mobile = models.CharField(_("Mobile"), max_length=40, null=True, blank=True)
    address = models.CharField(_("Address"), max_length=128, null=True, blank=True)
    ogrn_number = models.CharField(_("ОГРН"), max_length=13, null=True, blank=True)
    inn_number = models.CharField(_("ИНН"), max_length=10, null=True, blank=True)
    kpp_number = models.CharField(_("КПП"), max_length=9, null=True, blank=True)

    created_at = models.DateTimeField(_("created at"), auto_now_add=True, editable=False)
    last_modified = models.DateTimeField(_("last modified"), auto_now=True, editable=False)


    def __str__(self):
        return f"{self.name}"

    @property
    def phones(self):
        return ", ".join(filter(None, (self.phone, self.mobile)))
