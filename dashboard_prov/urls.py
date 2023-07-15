from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    
    path('dashboard_prov/', views.dashboard_prov, name='dashboard_prov'),

    path('solicitu_proyecto_prov/', views.solicitu_proyecto_prov, name='solicitu_proyecto_prov'),

    path('solicitu_enviar_acotizacion/<str:codigo_unico>/', views.solicitu_enviar_acotizacion, name='solicitu_enviar_acotizacion'),

    path('delete_solicitud_proyect_prov/<int:id>/', views.delete_solicitud_proyect_prov, name='delete_solicitud_proyect_prov'),

    

    path('proyecto_cotizacion_prov/', views.proyecto_cotizacion_prov, name='proyecto_cotizacion_prov'),

    path('aprovar_acotizacion/<str:codigo_unico>/', views.aprovar_acotizacion, name='aprovar_acotizacion'),

    path('proyecto_activado_prov/', views.proyecto_activado_prov, name='proyecto_activado_prov'),

    path('concluir_proyecto_activo/<str:codigo_unico>/', views.concluir_proyecto_activo, name='concluir_proyecto_activo'),

    path('suspender_proyecto_activo/<str:codigo_unico>/', views.suspender_proyecto_activo, name='suspender_proyecto_activo'),

    path('proyecto_suspendido_prov/', views.proyecto_suspendido_prov, name='proyecto_suspendido_prov'),

    path('reactivar_proyecto_suspendido/<str:codigo_unico>/', views.reactivar_proyecto_suspendido, name='reactivar_proyecto_suspendido'),

    path('cancelar_proyecto_suspendido/<str:codigo_unico>/', views.cancelar_proyecto_suspendido, name='cancelar_proyecto_suspendido'),


    path('cancelar_proyecto_activo/<str:codigo_unico>/', views.cancelar_proyecto_activo, name='cancelar_proyecto_activo'),

    path('proyecto_concluido_prov/', views.proyecto_concluido_prov, name='proyecto_concluido_prov'),

    path('proyecto_cancelado_prov/', views.proyecto_cancelado_prov, name='proyecto_cancelado_prov'),

    path('proyecto_detail_prov/<str:codigo_unico>/', views.proyecto_detail_prov, name='proyecto_detail_prov'),




    ########################### funcion del vendedor #############################################################
    path('Crear_nuevo_proyecto/<str:codigo_unico>/', views.Crear_nuevo_proyecto, name='Crear_nuevo_proyecto'),





    ################################## COMISIONES PENDIENTES ############################################
    path('proyecto_comision/', views.proyecto_comision, name='proyecto_comision'),

    path('saldar_comision/<str:codigo_unico>/', views.saldar_comision, name='saldar_comision'), 


    ################################## Comision Vendedor ##############################################

    path('list_comision_pendiente_vend/', views.list_comision_pendiente_vend, name='list_comision_pendiente_vend'),

    path('saldar_comision_vendedor/<str:codigo_unico>/', views.saldar_comision_vendedor, name='saldar_comision_vendedor'),

    ################################ HISTORIAL#############################################
    path('history_comision/', views.history_comision, name='history_comision'),
    path('history_comision_vendedores/', views.history_comision_vendedores, name='history_comision_vendedores'),
    path('history_afiliados_vendedores/', views.history_afiliados_vendedores, name='history_afiliados_vendedores'),



]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



