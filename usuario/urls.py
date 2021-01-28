from django.urls import path
from . import views
# Vistas propias de Django, para login y logout
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('lista/', views.lista, name='lista'),
    path('perfil/', views.perfil, name='perfil'),
    path('crear_usuario/', views.crear_usuario, name='crear_usuario'),
    path('login/',LoginView.as_view(template_name='usuario/login.html'), name="InicioSesion"),
    path('logout/',LogoutView.as_view(template_name='usuario/inicio.html'),name="Logout"),
]
