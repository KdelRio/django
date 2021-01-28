from django.contrib import admin
from usuario.models import Usuario,Empleado,Empresa_cliente

admin.site.register(Usuario)
admin.site.register(Empleado)
admin.site.register(Empresa_cliente)