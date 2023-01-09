from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from apps.aircraftblog.models import Tag, Category, AircraftItem, Manufacturer
from mptt.admin import MPTTModelAdmin


admin.site.register(Category , MPTTModelAdmin) 
@admin.register(Manufacturer)
class BrandAdmin(admin.ModelAdmin):   
    model = Manufacturer

    list_display = ('name', 'thumbnail_preview')
    readonly_fields = ('thumbnail_preview',)

    def thumbnail_preview(self, obj):
        return obj.thumbnail_preview

    thumbnail_preview.short_description = 'Thumbnail Preview'
    thumbnail_preview.allow_tags = True

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    model = Tag


@admin.register(AircraftItem)
class AircraftPostAdmin(ImportExportModelAdmin):
    model = AircraftItem

    list_display = (
        "id",
        "category",
        "type",
        "brand",
        "model",
        "family",
        "title",
        "subtitle",
        "slug",
        "publish_date",
        "published",
    )
    list_filter = (
        "published",
        "publish_date",
    )
    list_editable = (
        
    )
    search_fields = (
        "title",
        "subtitle",
        "slug",
        "body",
    )
    prepopulated_fields = {
        "slug": (
            "title",
            "subtitle",
        )
    }
    date_hierarchy = "publish_date"
    save_on_top = True

    class Meta:
        model = AircraftItem