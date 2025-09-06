# from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from config import settings

schema_view = get_schema_view(
   openapi.Info(
      title="FitClub Api",
      default_version='v1',
      description="Api for FitClub",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="makhliyoabboskhonova@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('apps.accounts.urls')),
    path('news/', include('apps.news.urls')),
    path('subscriptions/', include('apps.subscriptions.urls')),
    path('visits/', include('apps.visits.urls')),
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),


]