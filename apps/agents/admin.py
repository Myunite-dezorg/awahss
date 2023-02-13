from django.contrib import admin
from .models import Agent

@admin.register(Agent)
class AgentAdmin(admin.ModelAdmin):
    list_display = [
        'agent_id',
        'profile',
        'get_agent_name',
        'get_agent_phone',
        'barcode_preview'
    
   ]
    search_fields = ['profile__user__email','agent_id',]