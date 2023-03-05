from django.db import models
from datetime import date
import requests


class Airline(models.Model):
    iataCode = models.CharField(max_length=3)
    icaoCode = models.CharField(max_length=4)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Airport(models.Model):
    iataCode = models.CharField(max_length=3)
    icaoCode = models.CharField(max_length=4)

    def __str__(self):
        return self.iataCode


class Flight(models.Model):
    iataNumber = models.CharField(max_length=10, null=True)
    icaoNumber = models.CharField(max_length=10, null=True)
    number = models.CharField(max_length=10)

    def __str__(self):
        return self.number


class Schedule(models.Model):
    date = models.DateField(default=date.today)

    def __str__(self):
        return str(self.date)


class Departure(models.Model):
    iataCode = models.CharField(max_length=3)
    icaoCode = models.CharField(max_length=4)

    def __str__(self):
        return self.iataCode


class Arrival(models.Model):
    iataCode = models.CharField(max_length=3)
    icaoCode = models.CharField(max_length=4)

    def __str__(self):
        return self.iataCode


class FlightData(models.Model):
    airline = models.ForeignKey(Airline, on_delete=models.CASCADE)
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE)
    departure = models.ForeignKey(Departure, on_delete=models.CASCADE)
    arrival = models.ForeignKey(Arrival, on_delete=models.CASCADE)
    status = models.CharField(max_length=50, null=True)
    type = models.CharField(max_length=50, null=True)
