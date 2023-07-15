from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.conf import settings
import os
from .models import *
import uuid
from django.utils.text import slugify

#////////////////// PERFILDEL PROVEEDOR//////////////////
class Profile_proveedor(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE)
    
    codigo_unico_proveedor = models.CharField(
        max_length=7, 
        editable=False,
        unique=True,
        verbose_name="Código Único")
    
    image = models.ImageField(
        upload_to='imglogo', 
        null=True, 
        default="blank-profile-picture-gb46548963_1280.png", 
        verbose_name="Profile Image", 
        blank=True)
    
    nombre_empresa = models.CharField(
        max_length=50, 
        default='Nombre de mi empresa')
    
    configured = models.BooleanField(default=False)
    politicas = models.BooleanField(default=False)

    anio_nacimiento = models.PositiveIntegerField(null=True, blank=True, verbose_name="Año de Nacimiento")
    mes_nacimiento = models.PositiveIntegerField(null=True, blank=True, verbose_name="Mes de Nacimiento")
    dia_nacimiento = models.PositiveIntegerField(null=True, blank=True, verbose_name="Día de Nacimiento")

    def save(self, *args, **kwargs):
        if not self.codigo_unico_proveedor:
            slug = slugify(str(uuid.uuid4()))[:7]
            self.codigo_unico_proveedor = slug
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.user.username}'
    

#////////////////////codigo de confirmacion //////////////////
class Confirmacion(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    codigo = models.CharField(max_length=6)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    confirmado = models.BooleanField(default=False)
    
    def __str__(self):
        return f"Código de confirmación para {self.user.username}: {self.codigo}"