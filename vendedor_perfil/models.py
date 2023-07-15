from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from login_vendedor.models import Profile_vendedor
from perfil_proveedor.models import Profile_proveedor
from vend_config_inic.models import Contacto_vendedor
# Create your models here.




class Duda_comentario(models.Model):

    proveedor_fk = models.ForeignKey(
        Profile_proveedor, 
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    vendedor_fk = models.ForeignKey(
        Profile_vendedor,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    contact_vend_fk = models.ForeignKey(
        Contacto_vendedor,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    asunto_mensaage = models.CharField(
        max_length=100, 
        null=True, 
        blank=True,
        default="Null"

    )

    texto_mensage = models.CharField(
        max_length=2500, 
        null=True, 
        blank=True, 
        default='mensage'
    )

    fecha_mensage = models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name = 'duda_comentario'
        verbose_name_plural = 'duda_comentarios'

    def __str__(self):       
        return f'{self.asunto_mensaage} - {self.fecha_mensage}'
