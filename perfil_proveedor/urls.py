from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('registro_proveedor/', views.registro_proveedor, name='registro_proveedor'),
    path('confirm-email_proveedor/', views.send_confirmation_email, name='confirm-email_proveedor'),
    path('confirmar_proveedor/', views.confirmar_usuario, name='confirmar_proveedor'),
    path('nuevo_codigo/', views.enviar_nuevo_codigo, name='nuevo_codigo'),
    path('login_proveedor/', views.login_view, name='login_proveedor'),
    path('logout_view_proveedor/', views.logout_view, name='logout_view_proveedor'),
    path('recover_password/', views.recover_password, name='recover_password'),
    path('comprueba_perfil/', views.comprueba_perfil, name='comprueba_perfil'),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

