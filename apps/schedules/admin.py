from django.contrib import admin
from apps.profiles.models import Profile
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from import_export.admin import ImportExportModelAdmin
from import_export.widgets import TimeWidget
from import_export import resources
from import_export.fields import Field
from dynamic_raw_id.admin import DynamicRawIDMixin
from dynamic_raw_id.filters import DynamicRawIDFilter


from apps.schedules.models.flight_sched_model import Schedule, Airline, Arrival, Departure, Flight


class AirlineInline(admin.TabularInline):
    model = Airline
    extra = 0
class ArrivalInline(admin.TabularInline):
    model = Arrival
    extra = 0
class DepartureInline(admin.TabularInline):
    model = Departure
    extra = 0
class FlightInline(admin.TabularInline):
    model = Flight
    extra = 0


@admin.register(Schedule)
class ShedAdmin(DynamicRawIDMixin, ImportExportModelAdmin):  
    model = Schedule
    inlines = [
        AirlineInline,
        ArrivalInline,
        DepartureInline,
        FlightInline,
                
               ]

    list_display = (
        'status', 
        'type',  
    )
   