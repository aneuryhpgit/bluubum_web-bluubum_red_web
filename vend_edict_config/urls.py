from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [

    path('configuracion_vend/', views.configuracion_vend, name='configuracion_vend'),

    
    path('edit_email_vend/', views.edit_email_vend, name='edit_email_vend'),
    path('send_confir_email_vend/', views.send_confirmation_email_vend, name='send_confir_email_vend'),
    path('confir_cambio_email_vend/', views.confirmar_cambio_email_vend, name='confir_cambio_email_vend'),

    path('edit_username_vend/', views.edit_username_vend, name='edit_username_vend'),
    path('edit_password_vend/', views.edit_password_vend, name='edit_password_vend'),

    path('editar_foto_perfil_vend/', views.editar_foto_perfil_vend, name='editar_foto_perfil_vend'),
    path('editar_contacto_vend/', views.editar_contacto_vend, name='editar_contacto_vend'),
    path('editar_direccion_vend/', views.editar_ubicacion_vend, name='editar_direccion_vend'),
    path('edict_metodo_pago_vend/', views.metodo_pago_edict_vend, name='edict_metodo_pago_vend'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)