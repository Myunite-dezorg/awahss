from django.contrib import admin
from .models.aog_service_order import AogOrder



# class AOGItemInline(admin.TabularInline):
#     model = Aog
#     extra = 0

@admin.register(AogOrder)
class AogOrderAdmin(admin.ModelAdmin):
    list_display = [
        'order_number',
        'get_agent_id',
        'get_agent_profile_email',

    ]
    search_fields = ['order_number']

