from django.contrib import admin

# Register your models here.
from .models import Contacto_vendedor, Direccion_vendedor, Metodo_pago_vendedor
# Register your models here.





admin.site.register(Contacto_vendedor)

admin.site.register(Direccion_vendedor)

admin.site.register(Metodo_pago_vendedor)