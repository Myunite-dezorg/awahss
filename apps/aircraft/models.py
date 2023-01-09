from django.db import models
from django.utils.translation import gettext as _

# Create your models here.
class Aircraft(models.Model):
    iata_code = models.CharField(_("IATA"), max_length=3, default="")
    icao_code = models.CharField(_("ICAO"), max_length=4, default="")
    rus_name = models.CharField(_("Rus"), max_length=7, default="", blank=True)
    comment = models.CharField(_("Comment eng"), max_length=100, default="", blank=True)
    comment_rus = models.CharField(_("Comment rus"), max_length=100, default="", blank=True)
    public_name_eng = models.CharField(_("Public name eng"), max_length=155, default="", blank=True)
    public_name_rus = models.CharField(_("Public name rus"), max_length=155, default="", blank=True)
    
    def __str__(self):
        return self.icao_code
    