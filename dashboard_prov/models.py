from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from login_vendedor.models import Profile_vendedor
from perfil_proveedor.models import Profile_proveedor
from prov_servis.models import Servicio_prov
from vend_config_inic.models import Contacto_vendedor, Direccion_vendedor, Metodo_pago_vendedor
import uuid
from django.utils.text import slugify
# Create your models here.


class Afiliacion(models.Model):
    
    proveedor_afiliacion = models.ForeignKey(
        Profile_proveedor, 
        on_delete=models.CASCADE, 
        related_name='afiliaciones'
    )

    vendedor_afiliacion = models.ForeignKey(
        Profile_vendedor, 
        on_delete=models.CASCADE, 
        related_name='afiliaciones'
    )

    estado = models.CharField(
        max_length=20, 
        default='Aceptada'
    )

    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'afiliacion'
        verbose_name = 'afiliaciones'

    def __str__(self):
        return f'{self.proveedor_afiliacion} - {self.vendedor_afiliacion}'
    



class CrearProyecto(models.Model):
    
    afiliacion = models.ForeignKey(
        Afiliacion, on_delete=models.CASCADE, 
        related_name='servicios', 
        null=True,
        blank=True
    )
    

    proveedor = models.ForeignKey(
        Profile_proveedor, 
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    vendedor = models.ForeignKey(
        Profile_vendedor,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    contact_vendedor = models.ForeignKey(
        Contacto_vendedor,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    codigo_unico_proyect = models.CharField(
        max_length=15, 
        editable=False,
        unique=True,
        verbose_name="Código Único",
        null=True,
        blank=True
    )

    nombre_proyecto = models.CharField(
        max_length=100, 
        null=True, 
        blank=True,
        default="Null"

    )

    descripcion_proyecto = models.CharField(
        max_length=1030, 
        null=True, 
        blank=True, 
        default='Descripcion'
    )

    provincia_proyec = models.CharField(
        max_length=50, 
        null=True, 
        blank=True,
        default='Provincia'
    )

    ciudad_proyec = models.CharField(
        max_length=50, 
        null=True, 
        blank=True,
        default='Ciudad'
    )

    sector_proyec = models.CharField(
        max_length=50, 
        null=True, 
        blank=True,
        default='Sector'
    )

    calle_proyec = models.CharField(
        max_length=50, 
        null=True, 
        blank=True,
        default='calle'
    )

    numero_proyec = models.CharField(
        max_length=15, 
        null=True, 
        blank=True,
        default='numero'
    )

    apartamen_suite_proyec = models.CharField(
        max_length=15, 
        null=True, 
        blank=True,
        default='suite'
    )

    nombre_cliente = models.CharField(
        max_length=70, 
        null=True, 
        blank=True,
        default="Nombre cliente"
    )

    whatsapp = models.CharField(
        max_length=20, 
        default="000 000 0000", 
        null=True, 
        blank=True
    )

    telefono = models.CharField(
        max_length=20, 
        default="000 000 0000", 
        null=True, 
        blank=True
    )

    servicio = models.ForeignKey(
        Servicio_prov, 
        on_delete=models.CASCADE
    )

    fecha_solicitud = models.DateTimeField(auto_now_add=True)
    fecha_disponible_cotizacion = models.DateTimeField(null=True, blank=True)

    estado = models.CharField(
        max_length=30, 
        default="Pendiente"
    )

    precio = models.DecimalField(
        max_digits=15, 
        decimal_places=2, 
        null=True, 
        blank=True
    )

    vend_confir_precio = models.DecimalField(
        max_digits=15, 
        decimal_places=2, 
        null=True, 
        blank=True
    )

    comision_plataform = models.DecimalField(
        max_digits=15, 
        decimal_places=2, 
        default=0, 
        null=True, 
        blank=True,

    )
    
    #fecha de saldo de comision de la plataforma
    fecha_saldado_comis = models.DateTimeField(null=True, blank=True)

    estado_comis_plataform = models.CharField(
        max_length=20, 
        default="NULL"
    )


    comision_prov = models.DecimalField(
        max_digits=15, 
        decimal_places=2, 
        default=0, 
        null=True, 
        blank=True,

    )


    comision_vendedor = models.DecimalField(
        max_digits=15, 
        decimal_places=2, 
        default=0, 
        null=True, 
        blank=True
    )

    estado_de_comision_vend = models.CharField(
        max_length=12, 
        default="NULL"
    )



    #fecha programada de pago de comision a la plataforma
    fecha_pago_comision = models.DateTimeField(null=True, blank=True)
    #fecha programada de pago de comision al vendedor
    fecha_pago_comision_vend = models.DateTimeField(null=True, blank=True)


    fecha_aprobacion = models.DateTimeField(null=True, blank=True)

    fecha_estimada_inicio = models.DateTimeField(null=True, blank=True)
    fecha_estimada_conclusion = models.DateTimeField(null=True, blank=True)

    fecha_conclusion = models.DateTimeField(null=True, blank=True)

    fecha_suspencion_proyec = models.DateTimeField(null=True, blank=True)
    fecha_reanudacion_proyec = models.DateTimeField(null=True, blank=True)

    fecha_cancelacion_proyec = models.DateTimeField(null=True, blank=True)
    

    def save(self, *args, **kwargs):
        if not self.codigo_unico_proyect:
            slug = slugify(str(uuid.uuid4()))[:8]
            self.codigo_unico_proyect = slug
        super().save(*args, **kwargs)
    
    class Meta:
        verbose_name = 'crearproyecto'
        verbose_name_plural = 'crearproyectos'

    def __str__(self):       
        return f'{self.vendedor} - {self.servicio} - {self.fecha_solicitud} - {self.estado}'
    






############################################################################
######################### COMISION VENDEDOR  ###############################
############################################################################


class Comisiones_vendedor(models.Model):
    
    proyecto_comi = models.ForeignKey(
        CrearProyecto, on_delete=models.CASCADE, 
        related_name='proyecto_comision', 
        null=True,
        blank=True
    )

    proveedor_comi_fk = models.ForeignKey(
        Profile_proveedor, on_delete=models.CASCADE, 
        related_name='proveedor_comision_fk', 
        null=True,
        blank=True
    )

    vendedor_comi_fk = models.ForeignKey(
        Profile_vendedor, on_delete=models.CASCADE, 
        related_name='vendedor_comision_fk', 
        null=True,
        blank=True
    )

    direccion_comi_fk = models.ForeignKey(
        Direccion_vendedor, on_delete=models.CASCADE, 
        related_name='direc_vend_comision_fk', 
        null=True,
        blank=True
    )


    metd_pg_vend_comi_fk = models.ForeignKey(
        Metodo_pago_vendedor, on_delete=models.CASCADE, 
        related_name='mtd_pago_vend_comision_fk', 
        null=True,
        blank=True
    )

   
   #***************** Codigo factura ***************
    codigo_factura_comision_ved = models.CharField(
        max_length=17, 
        editable=False,
        unique=True,
        verbose_name="Código_factura_comisión",
        null=True,
        blank=True
    )


    institucion_deposito = models.CharField(
        max_length=40, 
        default="NULL",
        null=True,
        blank=True
    )


    fecha_facturacion = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.codigo_factura_comision_ved:
            slug = slugify(str(uuid.uuid4()))[:15]
            self.codigo_factura_comision_ved = slug
        super().save(*args, **kwargs)
    
    class Meta:
        verbose_name = 'comisiones_vendedor'
        verbose_name_plural = 'comisiones_vendedores'

    def __str__(self):       
        return f'{self.vendedor_comi_fk }'



    