from rest_framework import generics, serializers
from rest_framework.generics import ListAPIView
from apps.projects.models.flight_project import FlightProject
from .serializers import FlightProjectSerializer, RegisterSerializer, AirlineSerializer

class FlightProjectList(ListAPIView):
    serializer_class = FlightProjectSerializer

    def get_queryset(self):
        return FlightProject.postObjects.all()