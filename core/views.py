from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt



# Create your views here.
@csrf_exempt
def homepage(request):
    return render(request=request,
                  template_name='homepage.html')