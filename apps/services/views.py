import io
import os
import xlwt
from django.http import HttpResponse
from .models import AogService
from django.http import FileResponse
from django.shortcuts import render
from apps.schedules.models.sched import Schedule


def index(request):
    return render(request, 'index.html')

