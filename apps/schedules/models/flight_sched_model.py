# from django.db import models
# from apps.schedules.models.abstract import BaseSched
# from django.utils.translation import gettext_lazy as _


        

# class Schedule(BaseSched):
#     date = models.DateField(null=True)
#     status = models.CharField(_("Status"), max_length=20, null=True, blank=True)
#     type = models.CharField(_("Type"), max_length=20, null=True, blank=True)

#     def get_model_fields(airline):
#        return airline._meta.get_field('iataCode')
    
#     def get_model_fields(arrival):
#        return arrival._meta.get_field('iataCode')
    
#     def get_model_fields(departure):
#        return departure._meta.get_field('iataCode')
    
#     def get_model_fields(flight):
#        return flight._meta.get_field('iataNumber')
    
    
# class Airline(models.Model):
#     schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE, null=True)
#     iataCode = models.CharField(_("Iata code"), max_length=3, null=True, blank=True)
#     icaoCode = models.CharField(_("Icao code"), max_length=4, null=True, blank=True)
#     name = models.CharField(_("Name"), max_length=4, null=True, blank=True)

#     def __str__(self):
#         return f"{self.iataCode}"

# class Arrival(models.Model):
#     schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE, null=True)
#     actualTime = models.DateTimeField(null=True)
#     baggage = models.IntegerField(null=True)
#     delay = models.IntegerField(null=True)
#     estimatedRunway = models.DateTimeField(null=True)
#     estimatedTime = models.DateTimeField(null=True)
#     gate = models.IntegerField(null=True)
#     iataCode = models.CharField(_("Iata code"), max_length=4, null=True, blank=True)
#     icaoCode = models.CharField(_("Icao code"), max_length=4, null=True, blank=True)
#     scheduledTime = models.DateTimeField(null=True)
#     terminal = models.CharField(_("Terminal"), max_length=3, null=True, blank=True)


#     def __str__(self):
#         return f"{self.iataCode}"
    
# class Departure(models.Model):
#     schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE, null=True)
#     actualTime = models.DateTimeField(null=True)
#     baggage = models.IntegerField(null=True)
#     delay = models.IntegerField(null=True)
#     estimatedRunway = models.DateTimeField(null=True)
#     estimatedTime = models.DateTimeField(null=True)
#     gate = models.IntegerField(null=True)
#     iataCode = models.CharField(_("Iata code"), max_length=4, null=True, blank=True)
#     icaoCode = models.CharField(_("Icao code"), max_length=4, null=True, blank=True)
#     scheduledTime = models.DateTimeField(null=True)
#     terminal = models.CharField(_("Terminal"), max_length=3, null=True, blank=True)

#     def __str__(self):
#         return f"{self.iataCode}"


# class Flight(models.Model):
#     schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE, null=True)
#     iataNumber = models.CharField(_("Iata number"), max_length=5, null=True, blank=True)
#     icaoNumber = models.CharField(_("Icao number"), max_length=10, null=True, blank=True)
#     number = models.IntegerField(null=True)

#     def __str__(self):
#         return f"{self.iataNumber}"



# class codeshared(models.Model):
#     schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE, null=True)
#     airline = models.ForeignKey(Airline, on_delete=models.CASCADE, null=True)
#     flight = models.ForeignKey(Flight, on_delete=models.CASCADE, null=True)