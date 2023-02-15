from django.contrib import admin
from apps.services.models import AogService, DutyPerson, TASK_PRIORITY_FIELDS
from dynamic_raw_id.admin import DynamicRawIDMixin
from dynamic_raw_id.filters import DynamicRawIDFilter
from adminfilters.multiselect import UnionFieldListFilter
from django_admin_listfilter_dropdown.filters import RelatedDropdownFilter

from django.urls import reverse
from django.utils.html import format_html


class PersonInline(admin.TabularInline):
    model = DutyPerson
    extra = 0


@admin.register(AogService)
class AogServiceAdmin(admin.ModelAdmin):

    # def invoice_link(self, obj):
    #     if obj.id:
    #         url = reverse('services:export_invoice', args=[obj.id])
    #         return format_html('<a href="{}">Export to Excel</a>', url)
    #     return ''
    # invoice_link.short_description = 'Export to Excel'

    list_display = [
        'number',
        'request_date',
        'service_name',
        'flight',
        'created_by',



    ]
    list_display_links = ('number', 'flight')
    search_fields = ('id', 'service_name')
    list_filter = (
        # ('agent', RelatedDropdownFilter),
        # ('partner', RelatedDropdownFilter),
        ('type', UnionFieldListFilter),

    )
    ordering = TASK_PRIORITY_FIELDS
    readonly_fields = ('data_createAt', 'data_updateAt', 'created_by')

    # fieldsets = (               # Edition form
    #     (None,                   {'fields': ('service_name', ('user', 'partner'), 'deadline',
    #                                          ('state', 'priority'), ('description', 'resolution'))}),
    #     (_('More...'), {'fields': (('created_at', 'last_modified'), 'created_by'), 'classes': ('collapse',)}),
    # )

    inlines = [PersonInline]
