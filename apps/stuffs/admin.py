from django.contrib import admin
from apps.stuffs.models import Aog, AcEngine, StoreLocation

class StoreAdmin(admin.ModelAdmin):
    list_display = [
        'agent',
        'title',
    ]

class AogAdmin(admin.ModelAdmin):
    list_display = [
        'agent',
        'item_part_number',
        'item',
        'item_lenght',
        'item_width',
        'item_height',
        'item_weight',
        'is_serviceable'
    ]

    list_display_links = [
        'item_part_number'
    ]
    # list_editable = [
    #     'item',
    #     'item_lenght',
    #     'item_width',
    #     'item_height',
    #     'item_weight',
    #     'is_serviceable'
    # ]


class AcEngineAdmin(admin.ModelAdmin):
    list_display = [
        'pkid',
        'agent',
        'item',
        'item_weight',
        'item_serial_number',
        'item_part_number',
    ]


admin.site.register(Aog, AogAdmin)
admin.site.register(AcEngine, AcEngineAdmin)
admin.site.register(StoreLocation, StoreAdmin)
