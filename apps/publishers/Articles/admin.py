from django.contrib import admin
from .models import Category, Tag, Article
from mptt.admin import MPTTModelAdmin


admin.site.register(Category , MPTTModelAdmin) 



@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    model = Tag


@admin.register(Article)
class ArticlePostAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "category",
        "author",
        "title",
        "subtitle",
        "slug",
        "publish_date",
        "published",
        "feature_thumbnail_preview",
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


    
    def feature_thumbnail_preview(self, obj):
        return obj.feature_thumbnail_preview

    feature_thumbnail_preview.short_description = 'Feature Image Thumbnail Preview'
    feature_thumbnail_preview.allow_tags = True
    class Meta:
        model = Article