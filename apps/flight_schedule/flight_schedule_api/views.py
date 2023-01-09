from rest_framework import generics, serializers

from rest_framework.generics import ListAPIView
from apps.flight_schedule.models import FlightTask
from apps.directory.models import Register, Airline
from .serializers import TaskSerializer, RegisterSerializer, AirlineSerializer

class FlightTaskList(ListAPIView):
    serializer_class = TaskSerializer

    def get_queryset(self):
        return FlightTask.postObjects.all()

class AirlineList(ListAPIView):
    serializer_class = AirlineSerializer

    def get_queryset(self):
        return Airline.objects.all()


class RegisterList(ListAPIView):
    serializer_class = RegisterSerializer

    def get_queryset(self):
        return Register.objects.all()

# class RegisterList(generics.ListCreateAPIView):
#      queryset = Register.objects.all()
#      serializer_class = RegisterSerializer


# class AirlineList(generics.ListCreateAPIView):
#      queryset = Airline.objects.all()
#      serializer_class = AirlineSerializer
     

# class TaskList(ListAPIView):
#      serializer_class = TaskSerializer
#      def get_queryset(self):
#         return FlightTask.postObjects.all()

# class TaskList(generics.ListCreateAPIView):
#      queryset = FlightTask.postObjects.all()
#      serializer_class = TaskSerializer
     
     

# class TaskDeatil(generics.RetrieveDestroyAPIView):
#      queryset = FlightTask.objects.all()
#      serializer_class = TaskSerializer

