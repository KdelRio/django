from django.db import models
from django.utils import timezone
from django.dispatch import receiver
from allauth.account.signals import user_signed_up

class Empleado(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    rut = models.CharField(max_length=12, primary_key=True)
    telefono = models.IntegerField()
    sbruto = models.IntegerField()
    prevision = models.IntegerField()
    imposiciones = models.IntegerField()
    btransporte = models.IntegerField()
    badc = models.IntegerField()

class Empresa_cliente(models.Model):
    rutE = models.CharField(max_length=12, primary_key=True)
    nombreE = models.CharField(max_length=50)
    apellidoE = models.CharField(max_length=50)
    contraseñaE = models.CharField(max_length=50)
    correoE = models.CharField(max_length=50)
    telefonoE = models.IntegerField()
    tipo_cuenta = models.CharField(max_length=50)

class Usuario(models.Model):
    nombreU = models.CharField(max_length=50)
    apellidoU = models.CharField(max_length=50)
    correoU = models.CharField(max_length=12, primary_key=True)
    contraseñaU = models.CharField(max_length=50)
    telefonoU = models.IntegerField()

def create_user_profile(request, user, **kwargs):
    profile = Profile.objects.create(user=user)
    profile.save()