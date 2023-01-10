from django.contrib import admin
from django.urls import path, include, re_path
from apps.aircraft import views
from rest_framework import routers
from django.views.generic import TemplateView
from drf_yasg.views import get_schema_view  # new
from drf_yasg import openapi  # new
from rest_framework import permissions
from django.conf import settings
from django.conf.urls.static import static
from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView


from .views import homepage

schema_view = get_schema_view(  # new
    openapi.Info(
        title="Snippets API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    # url=f'{settings.APP_URL}/api/v3/',
    patterns=[path('api/', include('api.urls')), ],
    public=True,
    permission_classes=(permissions.AllowAny,),
)

router = routers.DefaultRouter()
router.register(r'aircrafts', views.AcViewSet())

urlpatterns = [
    path(  # new
        'swagger-ui/',
        TemplateView.as_view(
            template_name='swaggerui/swaggerui.html',
            extra_context={'schema_url': 'openapi-schema'}
        ),
        name='swagger-ui'),
    re_path(  # new
        r'^swagger(?P<format>\.json|\.yaml)$',
        schema_view.without_ui(cache_timeout=0),
        name='schema-json'),
    path('admin/', admin.site.urls),
    path('api/v1/', include("api.urls")), 
    path('flights/', include("apps.flight_schedule.urls", namespace='scheduler')),
    path("graphql", csrf_exempt(GraphQLView.as_view(graphiql=True))),
    path('tinymce/', include('tinymce.urls')),
    path('accounts/', include("apps.users.urls")),
    path('', homepage, name="index"),
] 
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
