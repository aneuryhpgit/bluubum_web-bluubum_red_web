from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [

    path('list_profil_prov/', views.vista_lista_proveedor, name='lista_perfil_prov'),

    path('proveedores-afiliados/<int:vendedor_id>/', views.proveedores_afiliados, name='proveedores_afiliados'),

    path('details_proyect/<str:codigo_unico>/', views.details_proyect, name='details_proyect'),

    path('edit_proyect_vend/<str:codigo_unico>/', views.edit_proyect_vend, name='edit_proyect_vend'),

    path('eliminar_proyecto/<int:id>/', views.eliminar_proyecto, name='eliminar_proyecto'),


    path('proyecto_pendiente_solic/', views.proyecto_pendiente_solic, name='proyecto_pendiente_solic'),  

    path('proyecto_cotizacion/', views.proyecto_cotizacion, name='proyecto_cotizacion'),
    
    path('proyecto_activo/', views.proyecto_activo, name='proyecto_activo'),

    path('proyecto_concluido/', views.proyecto_concluido, name='proyecto_concluido'),

    path('proyecto_suspendido/', views.proyecto_suspendido, name='proyecto_suspendido'),

    path('proyecto_delete/', views.proyecto_delete, name='proyecto_delete'),

    path('proyecto_historial/', views.proyecto_historial, name='proyecto_historial'),


    path('proyecto_comision_pendiente/', views.proyecto_comision_pendiente, name='proyecto_comision_pendiente'),

    path('factura_comision_vend/', views.factura_comision_vend, name='factura_comision_vend'),

    path('detail_factura_vendedor/<str:codigo_factura>/', views.detail_factura_vendedor, name='detail_factura_vendedor'),

    path('historial_de_pagos/', views.historial_de_pagos, name='historial_de_pagos'),

    path('create_message_duda_comentario/', views.create_message_duda_comentario, name='create_message_duda_comentario'),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)