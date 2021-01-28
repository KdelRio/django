from django.shortcuts import render
from .models import Empleado,Empresa_cliente,Usuario
from django.db import models

def inicio(request):
    return render(request, 'usuario/inicio.html', {})


def lista(request):

    empleado = Empleado.objects.all()

    return render(request, 'usuario/lista_empleados.html', {
        'empleado':empleado
    })

def perfil(request):
    return render(request, 'usuario/perfil.html', {})

def crear_usuario(request):
    return render(request, 'usuario/crear_usuario.html', {})

def login(request):
    return render(request, 'usuario/login.html', {})

def registro(request):
    return render(request, 'usuario/registro.html', {})