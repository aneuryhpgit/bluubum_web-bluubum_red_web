from django.contrib import admin

# Register your models here.
from .models import Profile_proveedor, Confirmacion


admin.site.register(Profile_proveedor)
admin.site.register(Confirmacion)