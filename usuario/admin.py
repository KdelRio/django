from django.contrib import admin
from .models import Usuario,Empleado,Empresa_cliente

admin.site.register(Usuario)
admin.site.register(Empleado)
admin.site.register(Empresa_cliente)