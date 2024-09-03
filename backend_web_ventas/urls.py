"""
URL configuration for backend_web_ventas project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# project/urls.py (archivo principal de URLs)
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# Swagger doc
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Web Doc",
      default_version='v1',
      description="Test description",
      terms_of_service="",
      contact=openapi.Contact(email="gaby13453@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
)
#

urlpatterns = [
    # Admin de django
    path('admin/', admin.site.urls),
    
    # url de login, sign up, etc
    path('accounts/', include('allauth.urls')),
    
    # Swagger
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    
    # APis:
    path('api/', include([
        # Pagina base
        path('main/', include('main.urls')),
        
        # Usuarios
        path('users/', include ('users.urls')),
        
        # Productos
        path('products/', include('products.urls')),
        
        # Servicios
        path('services/', include('services.urls')),
        
        # Lista de deseos
        path('favorites/', include('favorites.urls')),
    ])),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)