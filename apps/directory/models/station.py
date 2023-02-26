from django.db import models
import os
from django.utils.translation import gettext as _
from django.utils.text import slugify
from django.utils.html import mark_safe




def station_flag_directory_path(instance, filename):
        iata_name = slugify(instance.iata)
        icao_name = slugify(instance.icao)
        _, extension = os.path.splitext(filename)
        return f"stations/{iata_name}/{icao_name}{extension}"


class Station(models.Model):
    def image_upload_to(self, instance=None):
        if instance:
            return os.path.join('Stations', slugify(self.slug), instance)
        return None

    iata = models.CharField(_("IATA"), max_length=3, default="")
    icao = models.CharField(_("ICAO"), max_length=4, default="")
    rus = models.CharField(_("Rus"), max_length=5, default="")
    comment_eng = models.CharField(_("Comment Eng"), max_length=50, default="")
    comment_rus = models.CharField(_("Comment Rus"), max_length=50, default="")
    country = models.CharField(_("Country"), max_length=50, default="")
    city_r = models.CharField(_("Sity R"), max_length=50, default="")
    airport_e = models.CharField(_("Airport E"), max_length=50, default="")
    region = models.CharField(_("Region"), max_length=50, default="")
    airport_r = models.CharField(_("Airport R"), max_length=50, default="")
    city_e = models.CharField(_("City E"), max_length=50, default="")
    country_flag = models.ImageField(upload_to=station_flag_directory_path, blank=True, null=True)

    @property
    def thumbnail_preview(self):
        if self.country_flag:
            return mark_safe('<img src="{}" width="50" />'.format(self.country_flag.url))
        return ""
    
    
    def __str__(self):
        return f"{self.iata} | {self.icao}" 