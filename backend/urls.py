"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

#from django.views.generic import RedirectView

#from django.shortcuts import redirect

#def redirect_to_home(request):
 #   return redirect('home')

urlpatterns = [

    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('', include('perfil_proveedor.urls')),
    path('', include('config_inicial_prov.urls')),
    path('', include('configuracion_proveedor.urls')),
    path('', include('prov_servis.urls')),

    path('', include('login_vendedor.urls')),
    path('', include('vend_config_inic.urls')),
    path('', include('vend_edict_config.urls')),
    path('', include('dashboard_prov.urls')),
    path('', include('vendedor_perfil.urls')),
    path('', include('app_perfiles.urls')),

    # Ruta para redirigir URL no encontradas a la página de inicio
   # path('<path:undefined_path>', RedirectView.as_view(
    #   url='/'), name='redirect-to-home'),


]
