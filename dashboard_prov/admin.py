from django.contrib import admin

# Register your models here.
from .models import Afiliacion, CrearProyecto, Comisiones_vendedor
# Register your models here.


admin.site.register(Afiliacion)

admin.site.register(CrearProyecto)

admin.site.register(Comisiones_vendedor)