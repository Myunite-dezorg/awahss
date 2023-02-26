from django.contrib import admin
from apps.projects.models.flight_project import FlightProject, Tag 
from apps.projects.models.flight import Flight
from import_export.admin import ImportExportModelAdmin
from .forms import ProjectForm



class FlightInline(admin.TabularInline):
    model = Flight
    extra = 0



@admin.register(Tag)
class TagAdmin(ImportExportModelAdmin):
    list_display = [
        'name'
    ]


class ProjectAdmin(admin.ModelAdmin):
    form  = ProjectForm
    inlines = [FlightInline]
    @admin.display(description='project_date')
    def admin_project_date(self, obj):
        return obj.project_date.strftime('%d/%m/%Y')
    # @admin.display(description='sched_time')
    # def admin_sched_time(self, obj):
    #     return obj.sched_time.strftime('%H:%M')
    
    list_display = [
        'pkid',
        'user',
        'project_date',
        'project_name',
        'technology',
        'admin_project_date',
        'status'


        
    ]
    link_display = [
        'technology',
    ]
    list_editable = [
        'status'
    ]

    search_fields = ("project_name",)
    
    

admin.site.register(FlightProject, ProjectAdmin)


    
  
    
