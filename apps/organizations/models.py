from django.db import models
from apps.users.models import User
from django.utils.translation import gettext_lazy as _
from apps.organizations.uuid import BaseUUID


class Organization(BaseUUID):
    user = models.OneToOneField(User,  on_delete=models.CASCADE)
    # user = models.OneToOneField(User, on_delete=models.PROTECT)
    organization_name = models.CharField(
        _("Company Name"), max_length=50, default="Person Company LTD")
    address = models.TextField()
    ogrn_number = models.CharField(_("ОГРН"), max_length=13)
    inn_number = models.CharField(_("ИНН"), max_length=10)
    kpp_number = models.CharField(_("КПП"), max_length=9)
    website = models.URLField(_("Web Site Url"), max_length=200)

    def __str__(self):
        return f"{self.organization_name}"
