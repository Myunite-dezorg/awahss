from django.urls import path
from django.views.generic import TemplateView
from .views import index, FlightListView, flights_listing

app_name='flight_scheduler'

urlpatterns = [
    path('', index, name='index'),
    path('flights/', flights_listing, name='flights')
]
