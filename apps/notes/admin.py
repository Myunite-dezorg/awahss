from django.contrib import admin
from .models import Note, SharedBox, NoteShares, Collection, Category, Tag
from django.contrib.auth.admin import UserAdmin
from mptt.admin import MPTTModelAdmin

admin.site.register(Tag)

class CategoryAdmin(MPTTModelAdmin):
    model = Category

    list_display = ['name', 'slug']
    prepopulated_fields = {
        "slug": (
            "name",
        )
    }
admin.site.register(Category , CategoryAdmin) 

@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):   
    model = Note

    list_display = ('id', 'category', 'obj', 'author', 'title', 'slug',  'content', 'get_tags', 'createAt', 'updateAt',)

    prepopulated_fields = {
        "slug": (
            "title",
        )
    }

@admin.register(NoteShares)
class NoteSharesAdmin(admin.ModelAdmin):
    model = NoteShares

    list_display = ('id', 'owner', 'title',  'get_shared_with',  'parent',)



@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    model = Collection
    
    list_display = ['id',  'get_bookmark_url', ]

