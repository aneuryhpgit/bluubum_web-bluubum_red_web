from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [

    path('configuration_prov/', views.configuration_prov, name='configuration_prov'),

    #///////////////////////////// EDITAR USUARIO //////////////////////////////
    path('edit_email_prov/', views.edit_email_prov, name='edit_email_prov'),
    path('edit_username_prov/', views.edit_username_prov, name='edit_username_prov'),
    path('edit_password_prov/', views.edit_password_prov, name='edit_password_prov'),

    #///////////////////////////// EDITAR PERFIL //////////////////////////////
    path('editar_perfil_prov/',views.editar_perfil_prov, name='editar_perfil_prov'),


    #///////////////////////////// EDITAR CONTACTO //////////////////////////////
    path('editar_contacto_prov/', views.editar_contacto_prov, name='editar_contacto_prov'),

    #///////////////////////////// EDITAR UBICACION //////////////////////////////
    path('editar_ubicacion_prov/', views.editar_ubicacion_prov, name='editar_ubicacion_prov'),
    

    #///////////////////////////// EDITAR GEO_SERVICIOS //////////////////////////
    path('editar_geo_prov/', views.editar_geo_prov, name='editar_geo_prov'),

    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)