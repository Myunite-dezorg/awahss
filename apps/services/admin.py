from django.contrib import admin
from apps.services.models import AogService, DutyPerson
from dynamic_raw_id.admin import DynamicRawIDMixin
from dynamic_raw_id.filters import DynamicRawIDFilter




# class AogChangeList(ChangeList):
#     def __init__(self, request, model, list_display,
#                  list_display_links, list_filter, date_hierarchy,
#                  search_fields, list_select_related, list_per_page,
#                  list_max_show_all, list_editable, model_admin):
#         super(AogChangeList, self).__init__(request, model,
#                                             list_display, list_display_links, list_filter,
#                                             date_hierarchy, search_fields, list_select_related,
#                                             list_per_page, list_max_show_all, list_editable,
#                                             model_admin)

#         # these need to be defined here, and not in MovieAdmin
#         self.list_display = ['action_checkbox', 'item', 'service_item']
#         self.list_display_links = ['item']
#         self.list_editable = ['service_item']


class AogServiceAdmin(DynamicRawIDMixin, admin.ModelAdmin):

    list_display = [
        'service_name',
        'service_date',
        # 'get_changelist',
        # 'get_changelist_form',
        'agent',
        'flight',
        

    ]
     
    # autocomplete_fields = ['flight', ] 
    dynamic_raw_id_fields = ('flight',)
    # raw_id_fields = ('flight',)

    list_filter = (
        ('flight', DynamicRawIDFilter),
    )


class DutyPersonAdmin(admin.ModelAdmin):
    list_display = [
        'full_name',
        'position',
        'contact_phone',
    ]


admin.site.register(AogService, AogServiceAdmin)
admin.site.register(DutyPerson, DutyPersonAdmin)
