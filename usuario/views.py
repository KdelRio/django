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

    if request.POST:
        empleado = Empleado()
        empleado.nombre = request.POST.get('nombre')
        empleado.apellido = request.POST.get('apellido')
        empleado.rut = request.POST.get('rut')
        empleado.telefono = request.POST.get('telefono')
        empleado.sbruto = request.POST.get('sbruto')
        empleado.imposiciones = request.POST.get('imposiciones')
        empleado.prevision = request.POST.get('prevision')
        empleado.btransporte = request.POST.get('btransporte')
        empleado.badc = request.POST.get('badc')

        try:
            empleado.save()
        except:
            mensaje = "No se ha podido eliminar"
        return redirect('lista')

    return render(request, 'usuario/agregar.html', {})

def registro(request):
    return render(request, 'usuario/registro.html', {})

def eliminar_empleado(request,rut):

    empleado = Empleado.objects.get(rut=rut)

    try:
        empleado.delete()
    except:
        mensaje = "No se ha podido eliminar"
    return redirect('lista')

def modificar_empleado(request,rut):

    empleado = Empleado.objects.get(rut=rut)
    variables = {
        'empleado':empleado
    }

    if request.POST:
        empleado = Empleado()
        empleado.nombre = request.POST.get('nombre')
        empleado.apellido = request.POST.get('apellido')
        empleado.rut = request.POST.get('rut')
        empleado.telefono = request.POST.get('telefono')
        empleado.sbruto = request.POST.get('sbruto')
        empleado.imposiciones = request.POST.get('imposiciones')
        empleado.prevision = request.POST.get('prevision')
        empleado.btransporte = request.POST.get('btransporte')
        empleado.badc = request.POST.get('badc')

        try:
            empleado.save()
        except:
            mensaje = "No se ha podido eliminar"
        return redirect('lista')

    return render(request, 'usuario/modificar_empleado.html', variables)
