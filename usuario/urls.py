from django.urls import path
from . import views
from .views import inicio,lista,login,perfil,registro,eliminar_empleado,agregar,modificar_empleado,modificar_usuario,crear_empresa,lista_empresa,eliminar_empresa,modificar_empresa
# Vistas propias de Django, para login y logout
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('lista/', views.lista, name='lista'),
    path('agregar/', views.agregar, name='agregar'),
    path('registro/', views.registro, name='registro'),
    path('crear_empresa/', crear_empresa, name='crear_empresa'),
    path('lista_empresa/', views.lista_empresa, name='lista_empresa'),
    path('eliminar_empleado/<rut>/', eliminar_empleado, name='eliminar_empleados'),
    path('eliminar_empresa/<rutE>/', eliminar_empresa, name='eliminar_empresa'),
    path('modificar_empleado/<rut>/', modificar_empleado, name='modificar_empleado'),
    path('modificar_usuario/<correoU>/', modificar_usuario, name='modificar_usuario'),
    path('modificar_empresa/<rutE>/', modificar_empresa, name='modificar_empresa'),
    path('perfil/', views.perfil, name='perfil'),
    path('login/',LoginView.as_view(template_name='usuario/login.html'), name="InicioSesion"),
    path('login_facebook/',LoginView.as_view(template_name='usuario/login_facebook.html'), name="InicioFacebook"),
    path('logout/',LogoutView.as_view(template_name='usuario/inicio.html'),name="Logout"),
]
