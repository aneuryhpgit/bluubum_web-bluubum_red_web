from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('vista_perfil_proveedor/<str:codigo_unico>/', views.vista_perfil_proveedor, name='vista_perfil_proveedor'),

    path('vista_perfil_vend/<str:codigo_unico_vend>/', views.vista_perfil_vendedor, name='vista_perfil_vend'),

    path('afiliarme', views.afiliacion_view, name='afiliarme'),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)