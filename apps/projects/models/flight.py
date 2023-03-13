from django.db import models
from apps.projects.models.flight_project import FlightProject
from django.utils.translation import gettext as _
#
from apps.directory.models.airline import Airline
from apps.directory.models.register import Register
from apps.directory.models.airports import Airport
 
class Flight(models.Model):
    project = models.ForeignKey(FlightProject, on_delete=models.CASCADE, null=True)
    airline = models.ForeignKey(Airline, related_name='flight_airline', on_delete=models.PROTECT)
    registration = models.ForeignKey(Register, related_name='flight_register', on_delete=models.PROTECT)
    flight = models.CharField(_("Flight"), max_length=6, default="")
    sched_date =models.DateField(_("Schedule date"), auto_now=False, auto_now_add=False, null=True, blank=True)
    sched_time =models.TimeField(_("Schedule time"), auto_now=False, auto_now_add=False, null=True, blank=True)
    route = models.ForeignKey(Airport, related_name='flight_station', on_delete=models.PROTECT)


    def __str__(self):
        return f"{self.flight}/{self.sched_date}/{self.route}"