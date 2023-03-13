from django.db import models
import os
from django.utils.translation import gettext as _
from django.utils.text import slugify
from django.utils.html import mark_safe




def station_flag_directory_path(instance, filename):
        iata_name = slugify(instance.codeIataAirport)
        icao_name = slugify(instance.codeIcaoAirport)
        _, extension = os.path.splitext(filename)
        return f"stations/{iata_name}/{icao_name}{extension}"


class Airport(models.Model):
    def image_upload_to(self, instance=None):
        if instance:
            return os.path.join('Stations', slugify(self.slug), instance)
        return None

    
    gmt = models.CharField(max_length=6, null=True, blank=True)
    codeIataAirport = models.CharField(_("Airport IATA"), max_length=3, default="")
    codeIcaoAirport = models.CharField(_("Airport ICAO"), max_length=4, default="")
    codeIataCity = models.CharField(_("City IATA"), max_length=3, default="")
    codeIso2Country = models.CharField(_("ISO2Country"), max_length=2, default="")
    latitudeAirport = models.DecimalField(max_digits=16, decimal_places=12, blank=True, null=True)
    longitudeAirport = models.DecimalField(max_digits=16, decimal_places=12, blank=True, null=True)
    nameAirport = models.CharField(_("Airport name"), max_length=100, null=True, blank=True)
    nameCountry = models.CharField(_("Country name"), max_length=100, null=True, blank=True)
    phone = models.CharField(_("Phone"), max_length=50, null=True, blank=True)
    timezone = models.CharField(_("Zone"), max_length=100, null=True, blank=True)
    country_flag = models.ImageField(upload_to=station_flag_directory_path, blank=True, null=True)

    @property
    def thumbnail_preview(self):
        if self.country_flag:
            return mark_safe('<img src="{}" width="50" />'.format(self.country_flag.url))
        return ""
    
    
    def __str__(self):
        return f"{self.codeIataAirport} | {self.codeIcaoAirport}" 