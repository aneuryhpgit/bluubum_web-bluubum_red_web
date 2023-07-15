from django.contrib import admin

from django.db import models

from .models import Categoria, Articulo_blog, Imagen_itileria, Politicas
# Register your models here.


    

admin.site.register(Categoria)
admin.site.register(Articulo_blog)
admin.site.register(Imagen_itileria)
admin.site.register(Politicas)








