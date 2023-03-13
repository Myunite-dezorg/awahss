from django.contrib import admin
from django.http import HttpResponseRedirect
from import_export.admin import ImportExportModelAdmin
from apps.directory.models.airline import Airline
from apps.directory.models.register import Register
from apps.directory.models.airports import Airport
from django.urls import path, reverse
from .views import LinkAirlineImagesView


@admin.register(Airline)
class AilineAdmin(ImportExportModelAdmin):
    actions = ['link_images']

    def link_images(self, request, queryset):
        # Redirect to the LinkAirlineImagesView
        return HttpResponseRedirect(reverse('link_airline_images'))

    link_images.short_description = 'Link airline images'

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('link_airline_images/', LinkAirlineImagesView.as_view(), name='link_airline_images'),
        ]
        return my_urls + urls
    list_display = [
        'id',
        'thumbnail_preview',
        'banner_img',
        "ageFleet",
        "callsign",
        "codeHub",
        "codeIataAirline",
        "codeIcaoAirline",
        "codeIso2Country",
        "founding",
        "iataPrefixAccounting",
        "nameAirline",
        "nameCountry",
        "sizeAirline",
        "statusAirline",
        "type",

        
    ]
    search_fields = ['codeIataAirline','codeIcaoAirline', 'codeIso2Country',]
    
@admin.register(Register)
class RegisterAdmin(ImportExportModelAdmin):
    list_display = [
        
        'number',
        'ac_type',
        'co',
        'mod',
        'g_type',
        'description',
        'thumbnail_preview',

        
    ]
    search_fields = ['co','number']
    # list_editable = [
    #     'rus_name',
    #     'comment',
    #     'comment_rus',
    #     'public_name_eng',
    #     'public_name_rus'
        
    # ]
@admin.register(Airport)
class AirportAdmin(ImportExportModelAdmin):
    list_display = [
        
        'gmt',
        'codeIataAirport',
        'codeIcaoAirport',
        'codeIataCity', 
        'codeIso2Country',
        'latitudeAirport',
        'longitudeAirport',
        'nameAirport',
        'nameCountry',
        'phone',
        'timezone',
        'thumbnail_preview',

    ]
    search_fields = ['codeIataAirport','codeIcaoAirport', 'codeIso2Country', ]
    # list_editable = [
    #     'rus_name',
    #     'comment',
    #     'comment_rus',
    #     'public_name_eng',
    #     'public_name_rus'
        
    # ]