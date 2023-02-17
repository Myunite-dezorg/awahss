from .models import FlightTask
from django.contrib import admin
from django import forms
from django.utils.translation import gettext as _
from apps.directory.models import Register
from apps.payload.models import Payload
from django.contrib.admin.widgets import AutocompleteSelect

from django_select2 import forms as s2forms


class AirlineWidget(s2forms.ModelSelect2Widget):
    search_fields = [

        "icao__icontains",
        "iata__icontains",
        "rus_code__icontains",
        "comment_rus__icontains",
    ]


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
        widgets = {
            "airline": AirlineWidget,
        }

    payload = forms.CharField(max_length=50,
                              widget=forms.TextInput
                              (attrs={'placeholder': 'Enter some payload value ( kg )'}))


class RegisterForm(forms.Form):
    ac_type = forms.ModelMultipleChoiceField(queryset=Register.objects.all())
