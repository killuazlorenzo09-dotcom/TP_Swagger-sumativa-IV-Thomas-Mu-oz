# config/urls.py

from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import permissions

# Importaciones para Swagger
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Configuración de la información de tu API
schema_view = get_schema_view(
   openapi.Info(
      title="Documentación de la API de Tareas",
      default_version='v1',
      description="Documentación pública de la API de Tareas para el Trabajo Práctico",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="tu_email@ejemplo.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Rutas de tu API. Se accede a tu app mi_api a través de /api/
    path('api/', include('mi_api.urls')), 

    # Rutas de Swagger y Redoc
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'), # <-- URL principal de la documentación
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
