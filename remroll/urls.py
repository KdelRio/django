from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('usuario.urls')),
    path('', include('quickstart.urls')),
    path('accounts/', include('allauth.urls')),
    path('', include('pwa.urls')),
]
