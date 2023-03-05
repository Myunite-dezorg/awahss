from django.db import models
from django.utils.translation import gettext as _


class ShcMsgAbbr(models.Model):

    type = models.CharField(_("Type"), max_length=155, null=True, blank=True)
    code = models.CharField(_("Code"), max_length=5, null=True, blank=True)
    description = models.CharField(_("Description"), max_length=255, null=True, blank=True)


    def __str__(self):
        return self.code
    
    class Meta:
        verbose_name = "Message code"
        verbose_name_plural = "Message codes"