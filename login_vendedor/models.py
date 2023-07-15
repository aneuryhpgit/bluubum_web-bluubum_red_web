from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.conf import settings
import os
from .models import *
import uuid
from django.utils.text import slugify
from perfil_proveedor.models import Confirmacion
# Create your models here.

#////////////////// PERFILDEL VENDEDOR//////////////////
class Profile_vendedor(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE)
    
    codigo_unico_vendedor = models.CharField(
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
        if not self.codigo_unico_vendedor:
            slug = slugify(str(uuid.uuid4()))[:7]
            self.codigo_unico_vendedor = slug
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.user.username}'