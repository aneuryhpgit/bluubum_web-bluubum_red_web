from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('registro_vendedor/', views.registro_vendedor, name='registro_vendedor'),
    path('confirmar_usuario_vend/', views.confirmar_usuario_vend, name='confirmar_usuario_vend'),
    path('enviar_nuevo_codigo_vend/', views.enviar_nuevo_codigo_vendedor, name='enviar_nuevo_codigo_vend'),

    path('login_vnd/', views.login_vendedor, name='login_vnd'),
    path('logout_vnd/', views.logout_vendedor, name='logout_vnd'),

    path('restaurar_password/', views.restaurar_password, name='restaurar_password'),

    path('comprueba_perfil_vend/', views.comprueba_perfil_vend, name='comprueba_perfil_vend'),

    path('perfil_vendedor/', views.perfil_vendedor, name='perfil_vendedor'),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


