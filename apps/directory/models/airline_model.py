from django.db import models
import os
from django.utils.translation import gettext as _
from django.utils.text import slugify
from django.utils.html import mark_safe

class Airline(models.Model):
    def image_upload_to(self, instance=None):
        if instance:
            return os.path.join('Airlines', slugify(self.slug), instance)
        return None

    iata = models.CharField(_("Iata"), max_length=2, default="")
    icao = models.CharField(_("Icao"), max_length=3, default="")
    rus_code = models.CharField(_("Rus"), max_length=2, default="")
    comment_eng = models.CharField(
        _("Description eng"), max_length=85, default="")
    comment_rus = models.CharField(
        _("Description rus"), max_length=85, default="")
    country = models.CharField(_("Country"), max_length=85, default="")
    alliance = models.CharField(_("Alliance"), max_length=5, default="")
    lowcost = models.CharField(_("Lowcost"), max_length=1, default="")
    description = models.CharField(_("Description"), max_length=50, default="")
    arl_logo = models.ImageField(
        upload_to=airline_logo_directory_path, blank=True, null=True)
    banner_img = models.ImageField(
        upload_to=airline_banner_directory_path, blank=True, null=True)

    @property
    def thumbnail_preview(self):
        if self.arl_logo:
            return mark_safe('<img src="{}" width="50" />'.format(self.arl_logo.url))
        return ""

    def __str__(self):
        return f"{self.iata.upper()}/{self.icao.upper()}"
