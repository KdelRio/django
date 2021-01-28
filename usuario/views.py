from django.shortcuts import render

def inicio(request):
    return render(request, 'usuario/inicio.html', {})


def lista(request):
    return render(request, 'usuario/lista_empleados.html', {})

def perfil(request):
    return render(request, 'usuario/perfil.html', {})

def crear_usuario(request):
    return render(request, 'usuario/crear_usuario.html', {})

def login(request):
    return render(request, 'usuario/login.html', {})

def registro(request):
    return render(request, 'usuario/registro.html', {})