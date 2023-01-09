from django.shortcuts import render
from .models import Aircraft
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import AcSerializer
from rest_framework import routers, serializers, viewsets
from rest_framework import permissions


class AcViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Aircraft.objects.all()
    serializer_class = AcSerializer
    permission_classes = [permissions.IsAuthenticated]
