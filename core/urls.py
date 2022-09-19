from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from contact.views import *

schema_view = get_schema_view(
    openapi.Info(
        title="Contact API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://mediusware.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-doc/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('contacts/', ContactAPIView.as_view()),
    path('country-contacts/<str:country>/', CountryContactAPIView.as_view())
]

urlpatterns + static(settings.STATIC_URL, settings.STATIC_ROOT)
