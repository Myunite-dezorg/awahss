from django.contrib import admin
from .models import Agent

@admin.register(Agent)
class AgentAdmin(admin.ModelAdmin):
    list_display = [
        'agent_id',
        # 'barcode_preview'
       
]