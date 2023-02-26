from django.db import models
import os
from django.utils.translation import gettext as _
from django.utils.text import slugify
from django.utils.html import mark_safe



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