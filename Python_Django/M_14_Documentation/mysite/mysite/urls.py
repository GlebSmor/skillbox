"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns

from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

urlpatterns = [
   path('admin/doc/', include('django.contrib.admindocs.urls')),
   path('api/shema/', SpectacularAPIView.as_view(), name="shema"),
   path('api/shema/swagger/', SpectacularSwaggerView.as_view(url_name="shema"), name="swagger"),
   path('api/shema/redoc/', SpectacularRedocView.as_view(url_name="shema"), name="redoc"),
   path('api/', include('myapiapp.urls')),
]

urlpatterns += i18n_patterns(
    path('myauth/', include('myauth.urls')),
    path('shop/', include('shopapp.urls')),
    path('admin/', admin.site.urls),
    
)

if settings.DEBUG:
    urlpatterns.extend(
    static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    )