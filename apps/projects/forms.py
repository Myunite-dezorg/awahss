from apps.projects.models.flight_project import FlightProject
from django.contrib import admin
from django import forms
from django.utils.translation import gettext as _
from apps.directory.models.register import Register
from django.contrib.admin.widgets import AutocompleteSelect

from django_select2 import forms as s2forms


# class AirlineWidget(s2forms.ModelSelect2Widget):
#     search_fields = [

#         "icao__icontains",
#         "iata__icontains",
#         "rus_code__icontains",
#         "comment_rus__icontains",
#     ]


# class RegisterWidget(s2forms.ModelSelect2Widget):
#     search_fields = [

#         "number__icontains",

#     ]


class ProjectForm(forms.ModelForm):

    class Meta:
        model = FlightProject
        fields = [

            'user',
            'project_date',
            'project_name',
            'technology',
            'project_date',
            'tags',
            'status'

        ]
        
