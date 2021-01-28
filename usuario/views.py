from django.shortcuts import render
from django.shortcuts import redirect
from .models import Empleado,Empresa_cliente,Usuario

def inicio(request):
    return render(request, 'usuario/inicio.html', {})

def lista(request):

    empleado = Empleado.objects.all()

    return render(request, 'usuario/lista_empleados.html',{
        'empleado':empleado
    })

def perfil(request):
    return render(request, 'usuario/perfil.html', {})

def crear_usuario(request):
    return render(request, 'usuario/crear_usuario.html', {})

def login(request):
    return render(request, 'usuario/login.html', {})

def agregar(request):
    return render(request, 'usuario/agregar.html', {})

def registro(request):
    return render(request, 'usuario/registro.html', {})

def agregar(request):

    if request.POST:
        empleado = Empleado()
        nombre = request.POST.get('nombre'),
        apellido = request.POST.get('apellido'),
        rut = request.POST.get('rut'),
        telefono = request.POST.get('telefono'),
        sbruto = request.POST.get('sbruto'),
        prevision = request.POST.get('prevision'),
        imposiciones = request.POST.get('imposiciones'),
        btransporte = request.POST.get('btransporte'),
        badc = request.POST.get('badc')
    try:
        empleado.save()
    except:
            messages = 'no se pudo crear'
    return redirect('lista') 

def eliminar_empleado(request,rut):

    empleado = Empleado.objects.get(rut=rut)

    try:
        empleado.delete()
    except:
        mensaje = "No se ha podido eliminar"
    return redirect('lista')
