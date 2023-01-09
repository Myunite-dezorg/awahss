from django.contrib import admin
from .models import Note, SharedBox, NoteShares, Collection
from django.contrib.auth.admin import UserAdmin


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):   
    model = Note

    list_display = ('id', 'obj', 'author', 'title',  'content',  'createAt', 'updateAt',)

@admin.register(NoteShares)
class NoteSharesAdmin(admin.ModelAdmin):
    model = NoteShares

    list_display = ('id', 'owner', 'title',  'get_shared_with',  'parent',)



@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    model = Collection
    
    list_display = ['id',  'get_bookmark_url', ]

