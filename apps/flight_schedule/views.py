from django.template.response import TemplateResponse
from apps.flight_schedule.models import FlightTask
from apps.directory.models import Airline
from django_tables2 import SingleTableView
from django.shortcuts import render
 
from .tables import TasksTable
from django_tables2.config import RequestConfig
 

def flights_listing(request):
    config = RequestConfig(request)
    table1 = TasksTable(FlightTask.objects.filter(technology__contains=('arrival')), prefix="1-")  # prefix specified
    table2 = TasksTable(FlightTask.objects.filter(technology__contains=('departure')), prefix="2-")  # prefix specified
    config.configure(table1)
    config.configure(table2)

    return render(request, 'table_flights.html', {
        'table1': table1,
        'table2': table2
    })

 
def index(request):
    airl = Airline.objects.all()
    ftl = FlightTask.postObjects.all()
    context = {
        'ftl': ftl,
        'airl': airl
    }
    
    return TemplateResponse(request, 'index.html', context=context)


class FlightListView(SingleTableView):
    model = FlightTask
    table_class = TasksTable
    template_name = 'table_flights.html'
    # paginator_class = LazyPaginator