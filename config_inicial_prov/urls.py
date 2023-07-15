from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('bienvenida_proveedor/', views.bienvenida_proveedor, name='bienvenida_proveedor'),
    path('image_perfil_prov/', views.image_de_perfil_prov, name='image_perfil_prov'),
    path('config_inicial_contacto_prov/', views.config_ini_contacto_prov, name='config_ini_contacto_prov'),
    path('confini_ubicacion_prov/', views.config_ini_ubicacion_prov, name='confini_ubicacion_prov'),
    path('geo_servicios_prov/', views.geo_servicios, name='geo_servicios_prov'),
    path('mensage_bienvenida_proveedor/', views.mensage_bienvenida_proveedor, 
    name='mensage_bienvenida_proveedor')
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)