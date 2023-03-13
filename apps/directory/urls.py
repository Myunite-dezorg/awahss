from django.urls import path
from .views import LinkAirlineImagesView

urlpatterns = [
    path('link_airline_images/', LinkAirlineImagesView.as_view(), name='link_airline_images'),
]