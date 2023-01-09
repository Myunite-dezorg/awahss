from django.urls import path, include
from apps.flight_schedule.flight_schedule_api.views import FlightTaskList
from rest_framework import routers
from api.apps.users.views import *
from api.apps.profiles.views import *
from api.apps.notes.views import *
from .views import *

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'profiles', ProfileViewSet)
router.register(r'notes', NoteViewSet)
router.register('ping', PingViewSet, basename="ping")


urlpatterns = [
    path('scheduler/', FlightTaskList.as_view(), name="api_scheduler"),
    # path('users', include("api.apps.users.urls")),
    path('profiles', include("api.apps.profiles.urls")),
    path('', include(router.urls)),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name="sign_up"),
    path('verify_token/', TokenVerifyView.as_view(), name='token_verify')
]