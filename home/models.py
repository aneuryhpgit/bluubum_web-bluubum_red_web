from django.db import models
from django.contrib.auth.models import User




class Politicas(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    autor = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    fecha_publicacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo





class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Articulo_blog(models.Model):
    
    autor = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        default=1,
        limit_choices_to={'is_staff': True}  # Limitar a usuarios con estado de Staff
    )

    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    titulo = models.CharField(max_length=200)

    
    imagen = models.ImageField(upload_to='imagenes/', null=True, blank=True)
    contenido = models.TextField(null=True, blank=True)
    
    imagen_segun = models.ImageField(upload_to='imagenes/', null=True, blank=True)
    contenido_segun = models.TextField(null=True, blank=True)
    
    imagen_tre = models.ImageField(upload_to='imagenes/', null=True, blank=True)
    contenido_tre = models.TextField(null=True, blank=True)

    imagen_cuatro = models.ImageField(upload_to='imagenes/', null=True, blank=True)
    contenido_cuatro = models.TextField(null=True, blank=True)
    

    fecha_publicacion = models.DateTimeField(auto_now_add=True)
   

    def __str__(self):
        return self.titulo





class ImagenBanner(models.Model):
    imagen = models.ImageField(upload_to='imagenes_banner/')


class PaginaPrincipal(models.Model):
    titulo = models.CharField(max_length=200)
    banner_imagenes = models.ManyToManyField('ImagenBanner')
    contenido = models.TextField()
    enlaces_informativos = models.ManyToManyField('Articulo_blog')

    def __str__(self):
        return self.titulo
    



class Imagen_itileria(models.Model):

    img_banner_one = models.ImageField(upload_to='imagenes_banner/', null=True, blank=True)
    img_banner_two = models.ImageField(upload_to='imagenes_banner/', null=True, blank=True)
    img_banner_three = models.ImageField(upload_to='imagenes_banner/', null=True, blank=True)





#MOdelo mensage de contacto
class Message(models.Model):
    sender_name = models.CharField(max_length=100)
    sender_email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)