from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *
# from apps.profiles.views import ProfileDetailView, profile_detail

urlpatterns = [
    
   path('bookmark/collection/<int:pk>', CollectionBookmarkToggleView.as_view(), name='collection'),

]