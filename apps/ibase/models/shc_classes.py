from django.db import models
from django.utils.translation import gettext as _


class AwbAirlineCode(models.Model):
    airline_name = models.CharField(_("Airline name"), max_length=155, null=True, blank=True)
    iataCode = models.CharField(_("Iata code"), max_length=2, null=True, blank=True)
    awb_prefix = models.IntegerField(null=True, blank=True)
    country = models.CharField(_("Country"), max_length=155, null=True, blank=True)


    def __str__(self):
        return self.airline_name
    
    class Meta:
        verbose_name = "Airline code"
        verbose_name_plural = "Airline codes"