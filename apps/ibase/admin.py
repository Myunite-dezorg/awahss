from django.contrib import admin
from apps.ibase.models.shc_classes import AwbAirlineCode
from apps.ibase.models.msg_shc_classes import ShcMsgAbbr 
from import_export.admin import ImportExportModelAdmin

@admin.register(AwbAirlineCode)
class AilineAdmin(ImportExportModelAdmin):
    list_display = [
        
        'airline_name',
        'iataCode',
        'awb_prefix',
        'country',

        
    ]
    search_fields = [
     'iataCode',
     'awb_prefix',
     ]
    # list_editable = [
    #     'rus_name',
    #     'comment',
    #     'comment_rus',
    #     'public_name_eng',
    #     'public_name_rus'
        
    # ]

@admin.register(ShcMsgAbbr)
class AilineAdmin(ImportExportModelAdmin):
    list_display = [
        
        'code',
        'description',

        
    ]
    search_fields = [
     'code',
     ]
    # list_editable = [
    #     'rus_name',
    #     'comment',
    #     'comment_rus',
    #     'public_name_eng',
    #     'public_name_rus'
        
    # ]