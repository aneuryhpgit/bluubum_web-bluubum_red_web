from django.db import models
from perfil_proveedor.models import Profile_proveedor
# Create your models here.


class Contacto_proveedor(models.Model):
    numWhatsapp = models.CharField(
        max_length=20, null=True, default="000 000") 
    
    telefono = models.CharField(
        max_length=20, default="000 000")
     
    user = models.ForeignKey(
        Profile_proveedor, 
        on_delete=models.CASCADE, 
        null=True, 
        related_name='contacto_prov')
    
    class Meta:
        verbose_name = 'contacto_proveedor'
        verbose_name = 'contacto_proveedores'

    def __str__(self):       
        return f'{self.user}'


    


class Ubicacion_proveedor(models.Model):
    provicia = models.CharField(
        max_length=50, 
        default="provincia", 
        null=True)
    
    ciudad = models.CharField(
        max_length=50, 
        default="Ciudad", 
        null=True)
    
    calle = models.CharField(
        max_length=50, 
        default="Calle", 
        null=True)
    
    numero = models.CharField(
        max_length=10, 
        default="Numero", 
        null=True)
    
    user = models.ForeignKey(
        Profile_proveedor, 
        on_delete=models.CASCADE, 
        null=True, 
        related_name='ubicacion_prov')
    
    class Meta:
        verbose_name = 'ubicacion_proveedor'
        verbose_name = 'ubicacion_proveedores'

    def __str__(self):       
        return self.provicia




class Rango_servicio(models.Model):
    geo_servicio = models.CharField(
        max_length=50, default="Geo", 
        null=True)
    
    user = models.ForeignKey(
        Profile_proveedor, 
        on_delete=models.CASCADE, 
        null=True, 
        related_name='geo_servis')
    
    class Meta:
        verbose_name = 'rango_servicio'
        verbose_name = 'rango_servicios'

    def __str__(self):       
        return self.geo_servicio