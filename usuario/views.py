from django.shortcuts import render

def inicio(request):
    return render(request, 'usuario/inicio.html', {})

def lista_persona(request):
    return render(request, 'usuario/lista_persona.html', {})

def lista(request):
    return render(request, 'usuario/lista_persona.html', {})
