from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('bienvenida_vendedor', views.bienvenida_vendedor, name='bienvenida_vendedor'),
    path('foto_vendedor/', views.foto_vendedor, name='foto_vendedor'),
    path('config_ini_contacto_vendedor/', views.config_ini_contacto_vend, name='config_ini_contacto_vendedor'),
    path('config_ini_ubicacion_vend/', views.config_ini_ubicacion_vend, name='config_ini_ubicacion_vend'),
    path('metodo_pago_inic_vend/', views.metodo_pago_inic_vend, name='metodo_pago_inic_vend'),
    path('info_inic_vend/', views.info_inic_vend, name='info_inic_vend'),
    path('info_bienvenida_dos_vend/', views.info_bienvenida_dos_vend, name='info_bienvenida_dos_vend')

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)