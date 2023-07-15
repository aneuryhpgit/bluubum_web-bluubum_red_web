from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from login_vendedor.models import Profile_vendedor

# Create your models here.
class Contacto_vendedor(models.Model):
    telefono = models.CharField(
        max_length=20,  null=True) 
    
    numeroWhatsapp_afiliado = models.CharField(
        max_length=20, unique=True) 
    
    user = models.ForeignKey(
        Profile_vendedor, 
        on_delete=models.CASCADE, 
        null=True, 
        related_name='contato_afi')
    
    # Campos de fecha y hora para la creación y actualización
    creado_c_en = models.DateTimeField(auto_now_add=True)
    actualizado_c_en = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'contacto_afiliado'
        verbose_name = 'contacto_afiliados'

    def __str__(self):       
        return self.numeroWhatsapp_afiliado
    


class Direccion_vendedor(models.Model):
    provincia_afiliado = models.CharField(
        max_length=30, null=True, 
        default='provincia_afiliado')
    
    ciudad_afiliado = models.CharField(
        max_length=30, null=True, 
        default='ciudad_afiliado')
    
    sector_afiliado = models.CharField(
        max_length=70, null=True, 
        default='direccion_sector_afiliado')
    
    calle_afiliado = models.CharField(
        max_length=70, null=True, 
        default='direccion_sector_afiliado')
    
    numero = models.CharField(
        max_length=7, null=True, 
        default='000')
    
    apartamento_num = models.CharField(
        max_length=7, null=True, 
        default='00')
    
    user = models.ForeignKey(
        Profile_vendedor, 
        on_delete=models.CASCADE, 
        null=True, 
        related_name='direccion_afiliado_user')
    
    # Campos de fecha y hora para la creación y actualización
    creado_d_en = models.DateTimeField(auto_now_add=True)
    actualizado_d_en = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'direccion_afiliado'
        verbose_name = 'direccion_afiliados'

    def __str__(self):       
        return self.provincia_afiliado
    



class Metodo_pago_vendedor(models.Model):
    metodo_cobro = models.CharField(
        max_length=50, 
        blank=True, 
        null=True, 
        default="NULL")
    
    tipo_document_identificacion = models.CharField(
        max_length=15,
        null=True, 
        blank=True, 
        default="Cedula")

    
    Nombre_completo_identificacion = models.CharField(
        max_length=100, 
        null=True, 
        blank=True, 
        default="NULL")
    
    nombre_banco = models.CharField(
        max_length=50, 
        null=True, 
        blank=True, 
        default="NULL")
    
    Numero_cuenta_bancaria = models.CharField(
        max_length=100, 
        null=True, 
        blank=True, 
        default="XXXX XXXX XXXX")
    
    user = models.ForeignKey(
        Profile_vendedor, 
        on_delete=models.CASCADE, 
        null=True, 
        related_name='pago_afiliado')
    # Campos de fecha y hora para la creación y actualización
    creado_m_en = models.DateTimeField(auto_now_add=True)
    actualizado_m_en = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'metodo_pago_afiliado'
        verbose_name = 'metodo_pago_afiliados'

    def __str__(self):       
        return self.metodo_cobro