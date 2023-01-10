from django.contrib import admin
from apps.profiles.models import Profile
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import User


# class CustomUserAdmin(UserAdmin):
#     add_form = CustomUserCreationForm
#     form = CustomUserChangeForm
#     model = CustomUser
#     list_display = ['username', 'email', ]

admin.site.register(User)


# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):   
    model = Profile

    list_display = ('id', 'user',  'full_name', 'phone', 'birthday', 'shift_work', 'thumbnail_preview')
    readonly_fields = ('thumbnail_preview',)

    def thumbnail_preview(self, obj):
        return obj.thumbnail_preview

    thumbnail_preview.short_description = 'Thumbnail Preview'
    thumbnail_preview.allow_tags = True