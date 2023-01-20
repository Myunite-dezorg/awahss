from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .models import Organization


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phones', 'address',)
    list_display_links = ('id', 'name')
    search_fields = ('id', 'name', 'email')

    ordering = ('name',)
    # list_filter = ('is_company',)
    readonly_fields = ('created_at', 'last_modified', )
    fieldsets = (  # Edition form
        (None, {'fields': ( ('email', 'website'), ('phone', 'mobile'), ('address',))}),
        (_('More...'), {'fields': (('created_at', 'last_modified'),  ('ogrn_number', 'inn_number', 'kpp_number' )),  'classes': ('collapse',)}),
    )

    def get_fieldsets(self, request, obj=None):
        fieldsets = super().get_fieldsets(request, obj)
        if obj is None:
            fieldsets = (      # Creation form
                (None, {'fields': (('name'), ('email', 'website'), ('phone', 'mobile'), ('address',))}),
            )
        return fieldsets

    # def save_model(self, request, obj, form, change):
    #     if change is False:
    #         obj.created_by = request.user
    #     super().save_model(request, obj, form, change)
