from django.urls import path
from .views import *
from . import views

app_name='schedule'

urlpatterns = [
    # path('flight-data/', fetch_flight_data, name='flights'),
    # path('fetch-flights/', views.fetch_and_insert_flights, name='fetch_flights'),
    path('flights/', flight_list, name='flight_list'),
]
