from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [

    path('crea_servicio_prov/', views.crear_servicio, name='crea_servicio_prov'),
    path('editar_servicio/<int:id>/', views.editar_servicio_prov, name='editar_servicio'),
    path('eliminar_servicio_prov/<int:id>/', views.eliminar_servicio_prov, name='eleiminar_servicio_prov'),


    #/////////////////////////// POST ////////////////////////////////////////
    path('creardor_post_serv/', views.crear_post_prov, name='creador_post_serv'),
    path('post_editor/<int:id>/', views.editar_post, name='post_editor'),
    path('eliminar_post_proveedor/<int:id>/', views.eliminar_post_prov, name='eliminar_post_proveedor'),

    #//////////////////////////// VISTAS SERVICIO Y POST /////////////////////
    path('vista_servicios/', views.vista_servicios, name='vista_servicios'),
    path('post_vista/<slug:slug>/', views.post_vista_list, name='post_vista'),
    path('post_detail/<slug:slug>/', views.detail_post, name='post_detail'),
   
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)