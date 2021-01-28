from django.shortcuts import render
from django.http import HttpResponse

def inicio(request):
    return render(request, 'usuario/inicio.html', {})


def lista(request):
    return render(request, 'usuario/lista_empleados.html', {})

def perfil(request):
    return render(request, 'usuario/perfil.html', {})

def crear_usuario(request):
    return render(request, 'usuario/crear_usuario.html', {})