from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
import os
from perfil_proveedor.models import Profile_proveedor
from config_inicial_prov.models import Contacto_proveedor, Ubicacion_proveedor, Rango_servicio
from django.utils.text import slugify
from django.utils import timezone
import uuid
# Create your models here.



def tumtu_directory_path(instance, filename):
    banner_pic_name = f"carServicios/servicio/{instance.nombre_servicio}/{filename}"
    full_path = os.path.join(settings.MEDIA_ROOT, banner_pic_name)

    if os.path.exists(full_path):
        os.remove(full_path)

    return banner_pic_name


class Servicio_prov(models.Model):
    nombre_servicio = models.CharField(
        max_length=50, default=None, 
        blank=True, null=True)
    
    imagen_servicio = models.ImageField(
        upload_to=tumtu_directory_path,
        height_field=None,
        width_field=None,
        default="NULL"
    )

    descripcion_serv = models.CharField(
        max_length=150, 
        default="NULL",
        blank=True,
        null=True
    )
    
    Comicion = models.DecimalField(
        max_digits=20,
        decimal_places=2,
        default=0.00
        )
    timestamp = models.DateTimeField(default=timezone.now)
    slug = models.SlugField(
        max_length=200,
        null=True,
        blank=True,
        unique=True
    )

    user = models.ForeignKey(
        Profile_proveedor, 
        on_delete=models.CASCADE, 
        null=True, 
        related_name='servicio')
    
    contactoProveedor_forenkey = models.ForeignKey(
        Contacto_proveedor,
        on_delete=models.CASCADE
    )

    ubicacionProveedor_forenkey = models.ForeignKey(
        Ubicacion_proveedor,
        on_delete=models.CASCADE
    )

    geoServiciosProveedor_forenkey = models.ForeignKey(
        Rango_servicio,
        on_delete=models.CASCADE
    )
    

    class Meta:
        verbose_name = 'servicio'
        verbose_name = 'servicios'
    
    def save(self, *args, **kwargs):
        if not self.slug and self.nombre_servicio:
            timestamp = timezone.now().strftime('%f')
            tien = self.user.nombre_empresa
            sif = slugify(str(uuid.uuid4()))[:36]
            self.slug = slugify(self.nombre_servicio + '-' + timestamp + str(self.user.id) + '-' + tien + '-' +sif)

        super().save(*args, **kwargs)







#/////////////////////////////////// POST DE LOS SERVICIOS ////////////////////////////


def imgpost_directory_path(instance, filename):
    post_serv_image = f"carpPostServ/servicioPost/{instance.titulo}/{filename}"
    full_path = os.path.join(settings.MEDIA_ROOT, post_serv_image)

    if os.path.exists(full_path):
        os.remove(full_path)

    return post_serv_image



class Post_prov(models.Model):
    imagen_serv = models.ImageField(
        upload_to=imgpost_directory_path,
        max_length=255,
        height_field=None,
        width_field=None,
        default="NULL"
    )
    imagen_serv_dos = models.ImageField(
        upload_to=imgpost_directory_path,
        max_length=255,
        height_field=None,
        width_field=None,
        default="NULL"
    )
    imagen_serv_tres = models.ImageField(
        upload_to=imgpost_directory_path,
        max_length=255,
        height_field=None,
        width_field=None,
        default="NULL"
    )
    imagen_serv_cuatro = models.ImageField(
        upload_to=imgpost_directory_path,
        max_length=255,
        height_field=None,
        width_field=None,
        default="NULL"
    )
    titulo = models.CharField(max_length=200)
    archivo_contenido = models.TextField() 

    slug = models.SlugField(
        max_length=200,
        null=True,
        blank=True,
        unique=True
    )

    user = models.ForeignKey(
        Profile_proveedor, 
        on_delete=models.CASCADE, 
        null=True, 
        related_name='posts')

    servicio = models.ForeignKey(
        Servicio_prov,
        on_delete=models.CASCADE
    )

    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)


    def content_directory_path(instance, filename):
        content_filename = f"{filename}.txt" # Establece el nombre de archivo como el nombre original más ".txt"
        content_path = f"Contenido/servicioPost/{instance.archivo_contenido}/{content_filename}"
        full_path = os.path.join(settings.MEDIA_ROOT, content_path)

        with open(full_path, 'wb') as file:
            file.write(instance.archivo_contenido.encode()) # Escribe el contenido del archivo en el directorio

        instance.archivo_contenido = content_filename # Establece el nombre del archivo en el campo
        instance.save()

        return content_path
    

    class Meta:
        verbose_name = 'Post_serv'
        verbose_name = 'Post_servs'
    

    def save(self, *args, **kwargs):
        if not self.slug and self.titulo:
            timestamp = timezone.now().strftime('%f')
            tien = self.titulo
            self.slug = slugify(self.titulo + '-' + timestamp + str(self.user.id) + '-' + tien)

        super().save(*args, **kwargs)
