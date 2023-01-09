from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from .models import Aircraft


@admin.register(Aircraft)
class AcAdmin(ImportExportModelAdmin):
    list_display = [
        'pk',
        'iata_code',
        'icao_code',
        'rus_name',
        'comment',
        'comment_rus',
        'public_name_eng',
        'public_name_rus'
        
    ]
    list_editable = [
        'rus_name',
        'comment',
        'comment_rus',
        'public_name_eng',
        'public_name_rus'
        
    ]
    


