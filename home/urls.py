from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [

    path('', views.home_page, name='home_page'),
    path('politicas_vend/', views.politicas_privacidad_user_vend, name='politicas_vend'),
    path('terminos_vend/', views.terminos_user_vend, name='terminos_vend'),

    path('message/', views.message_form, name='message_form'),
    path('message/list/', views.message_list, name='message_list'),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
