from django.contrib import admin
from apps.profiles.models import Profile
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from import_export.admin import ImportExportModelAdmin
from import_export.widgets import TimeWidget
from import_export import resources
from import_export.fields import Field
from dynamic_raw_id.admin import DynamicRawIDMixin
from dynamic_raw_id.filters import DynamicRawIDFilter


from .models import RegularScheduler

# class ScheduleResource(resources.ModelResource):
#     tech_route = Field(attribute='tech_route', column_name='tech_route') 
#     flt_number = Field(attribute='flt_number', column_name='flt_number') 
#     airport = Field(attribute='airport', column_name='airport') 
#     sta = Field(attribute='sta', column_name='sta',  widget=TimeWidget('<time_format>')) 
#     pta = Field(attribute='pta', column_name='pta',  widget=TimeWidget('<time_format>')) 
#     ata = Field(attribute='ata', column_name='ata',  widget=TimeWidget('<time_format>')) 
#     ...
#     class Meta:
#         model = RegularScheduler
#         fields = ('tech_route', 'flt_number', 'airport', 'sta', 'pta', 'ata',)



@admin.register(RegularScheduler)
class ShedAdmin(DynamicRawIDMixin, ImportExportModelAdmin):  
    # resource_class = ScheduleResource 
    model = RegularScheduler
    # sta = Field(column_name='sta', widget=TimeWidget(format="%H:%M:%S"))
    # pta = Field(column_name='pta', widget=TimeWidget(format="%H:%M:%S"))
    # ata = Field(column_name='ata', widget=TimeWidget(format="%H:%M:%S"))
    # std = Field(column_name='std', widget=TimeWidget(format="%H:%M:%S"))
    # ptd = Field(column_name='ptd', widget=TimeWidget(format="%H:%M:%S"))
    # atd = Field(column_name='atd', widget=TimeWidget(format="%H:%M:%S"))


    list_display = ('tech_rout', 'flt_number',  'airport', 'sta', 'pta', 'ata', 'std', 'ptd', 'atd')
    search_fields = ['flt_number','airport']

    
    
    # list_display_links = ['flt_number']