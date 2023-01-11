from django.contrib import admin
from .models import DCategory, DGRClass
from import_export.admin import ImportExportModelAdmin
from mptt.admin import MPTTModelAdmin


class CategoryAdmin(MPTTModelAdmin):
    list_display = [
        "category_name",
        "description",
        "parent",
    

    ]


admin.site.register(DCategory, MPTTModelAdmin)

@admin.register(DGRClass)
class DClassAdmin(ImportExportModelAdmin):   
    model = DGRClass

    list_display = (
        'category',
        'dgr_class',
        'name',
        'imp_code1',
        "cao",
        'imp_code2',
        'imp_code3',
        'label_preview',

         )
    readonly_fields = ('label_preview',)

    search_fields = (
        "category",
        "imp_code1",
        "imp_code2",
        "dgr_class",
    )

    def label_preview(self, obj):
        return obj.label_preview

    label_preview.short_description = 'Label Preview'
    label_preview.allow_tags = True

