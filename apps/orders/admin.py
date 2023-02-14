from django.contrib import admin
from .models.aog_service_order import AogOrder


@admin.register(AogOrder)
class AogOrderAdmin(admin.ModelAdmin):
    list_display = [
        # 'order_number',
        # 'order_tech',
        # 'order_date',

    ]
    search_fields = ['order_number']
