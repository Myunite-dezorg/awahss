from .models import FlightTask
from django.contrib import admin
from django import forms
from django.utils.translation import gettext as _
from apps.directory.models import Register
from apps.payload.models import Payload
from django.contrib.admin.widgets import AutocompleteSelect


class TaskForm(forms.ModelForm):
    
    
    class Meta:
        model = FlightTask
        fields = [
            'user',  
            'task_date', 
            'technology', 
            'airline',
            'registration',
            'flight',
            'sched_time', 
            'route', 
            'payload', 
            'payload_item',
            'description', 
            'status', 
            'tags',
            'docs',
            
        ]
        
    payload= forms.CharField(max_length=50,
                           widget= forms.TextInput
                           (attrs={'placeholder':'Enter some payload value ( kg )'}))
        
    
class RegisterForm(forms.Form):
   ac_type = forms.ModelMultipleChoiceField(queryset=Register.objects.all())
    