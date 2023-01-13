from django.contrib import admin
from .models import ImpCode
from import_export.admin import ImportExportModelAdmin


@admin.register(ImpCode)
class MsgTypeAdmin(ImportExportModelAdmin):
    list_display = [
        
        'type',
        'code',
        'description',

        
    ]
    search_fields = ['code',]
   
