from django.urls import path
from .views import *

app_name='schedule'

urlpatterns = [
    path('flight-data/', fetch_flight_data, name='flights'),
]
