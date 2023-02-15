from django.contrib import admin
from .models.aog_service_order import AogOrder

from django.urls import reverse
from django.utils.html import format_html



# class AOGItemInline(admin.TabularInline):
#     model = Aog
#     extra = 0

@admin.register(AogOrder)
class AogOrderAdmin(admin.ModelAdmin):
    
    # def invoice_link(self, obj):
    #     if obj.id:
    #         url = reverse('services:export_invoice', args=[obj.id])
    #         return format_html('<a href="{}">Export to Excel</a>', url)
    #     return ''
    # invoice_link.short_description = 'Export to Excel'
    
    list_display = [
        'order_number',
        'get_agent_id',
        'get_agent_profile_email',


    ]
    search_fields = ['order_number']

