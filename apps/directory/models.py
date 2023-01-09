from django.db import models
import os
from django.utils.translation import gettext as _
from django.utils.text import slugify
from django.utils.html import mark_safe

def airline_logo_directory_path(instance, filename):
        iata = slugify(instance.iata)
        icao = slugify(instance.icao)
        _, extension = os.path.splitext(filename)
        return f"airlines/{iata}/{icao}{extension}"

def airline_banner_directory_path(instance, filename):
        iata = slugify(instance.iata)
        icao = slugify(instance.icao)
        _, extension = os.path.splitext(filename)
        return f"airlines/banners/{iata}/{icao}{extension}"

class Airline(models.Model):
    def image_upload_to(self, instance=None):
        if instance:
            return os.path.join('Airlines', slugify(self.slug), instance)
        return None


    iata = models.CharField(_("Iata"), max_length=2, default="")
    icao = models.CharField(_("Icao"), max_length=3, default="")
    rus_code = models.CharField(_("Rus"), max_length=2, default="")
    comment_eng = models.CharField(_("Description eng"), max_length=85, default="")
    comment_rus = models.CharField(_("Description rus"), max_length=85, default="")
    country = models.CharField(_("Country"), max_length=85, default="")
    alliance = models.CharField(_("Alliance"), max_length=5, default="")
    lowcost = models.CharField(_("Lowcost"), max_length=1, default="")
    description = models.CharField(_("Description"), max_length=50, default="")
    arl_logo = models.ImageField(upload_to=airline_logo_directory_path, blank=True, null=True)
    banner_img = models.ImageField(upload_to=airline_banner_directory_path, blank=True, null=True)


    @property
    def thumbnail_preview(self):
        if self.arl_logo:
            return mark_safe('<img src="{}" width="50" />'.format(self.arl_logo.url))
        return ""


    def __str__(self):
        return f"{self.iata.upper()}/{self.icao.upper()}"

def airline_logo_directory_path(instance, filename):
        iata_name = slugify(instance.iata)
        icao_name = slugify(instance.icao)
        _, extension = os.path.splitext(filename)
        return f"Codespics/{iata_name}/{icao_name}{extension}"

def register_photo_directory_path(instance, filename):
        co = slugify(instance.co)
        number = slugify(instance.number)
        ac_type = slugify(instance.ac_type)
        _, extension = os.path.splitext(filename)
        return f"aircrafts/{co}/{number}/{ac_type}{extension}"
    
class Register(models.Model):

    number = models.CharField(_("Number"), max_length=5, default="")
    ac_type = models.CharField(_("Type"), max_length=3, default="")
    co = models.CharField(_("Company"), max_length=5, default="")
    mod = models.CharField(_("Modification"), max_length=4, default="")
    g_type = models.CharField(_("G_TYPE"), max_length=5, default="")
    description = models.CharField(_("Description"), max_length=50, default="")
    ac_photo = models.ImageField(upload_to=register_photo_directory_path, blank=True, null=True)
    
    @property
    def thumbnail_preview(self):
        if self.ac_photo:
            return mark_safe('<img src="{}" width="50" />'.format(self.ac_photo.url))

            
        return ""
    def __str__(self):
        return f"{self.number}"
    


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