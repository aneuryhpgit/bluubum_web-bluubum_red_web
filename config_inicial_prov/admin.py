from django.contrib import admin
from .models import Contacto_proveedor, Ubicacion_proveedor, Rango_servicio
# Register your models here.


admin.site.register(Contacto_proveedor)

admin.site.register(Ubicacion_proveedor)

admin.site.register(Rango_servicio)