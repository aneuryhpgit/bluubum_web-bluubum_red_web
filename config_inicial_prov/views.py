from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.conf import settings
from .models import *
from perfil_proveedor.models import Profile_proveedor
from storages.backends.gcloud import GoogleCloudStorage
from django.conf import settings


# Create your views here.



@login_required
def bienvenida_proveedor(request):
    
    return render(request, 'proveedor/confi_inicial/bienvenida_prov.html')


@login_required
def image_de_perfil_prov(request):
    show_message_error = False

    try:
        profile = Profile_proveedor.objects.get(user=request.user)
    except Profile_proveedor.DoesNotExist:
        profile = Profile_proveedor.objects.create(user=request.user)

    if request.method == 'POST':
        logo = request.FILES.get("imagen-logo")
        nombreEmpresa = request.POST.get("nombre_empresa")

        if logo != None and nombreEmpresa != None:

            image_logo_path = f'{settings.PUBLIC_MEDIA_LOCATION}/{logo.name}'
            storage = GoogleCloudStorage()
            storage.save(image_logo_path, logo)
            profile.image = image_logo_path

            profile.nombre_empresa=nombreEmpresa
            profile.save()

            return redirect('config_ini_contacto_prov')
        
        else:
            show_message_error = True
            return redirect('image_perfil_prov')
        
    context = {
        'show_message_error': show_message_error
    }


    return render(request, 'proveedor/confi_inicial/confg_ini_imagen_perfil_prov.html', context)




@login_required
def config_ini_contacto_prov(request):
    show_message_error = False

    try:
        profile = Profile_proveedor.objects.get(user=request.user)
        contacto = Contacto_proveedor.objects.get(user=profile)
    except Profile_proveedor.DoesNotExist:
        profile = None
        contacto = None
    except Contacto_proveedor.DoesNotExist:
        contacto = Contacto_proveedor(user=profile)
        contacto.save()

    if request.method == 'POST':    
        numero_whatsapp = request.POST.get("numero_whatsapp")
        numero_telefono = request.POST.get("numero_telefono")

        if numero_whatsapp != None and numero_telefono != None:
            
            contacto.numWhatsapp = numero_whatsapp
            contacto.telefono = numero_telefono
            contacto.save()

            return redirect('confini_ubicacion_prov')
        
        else:
            show_message_error = True
            return redirect('config_ini_contacto_prov')
        
    context = {
        'show_message_error': show_message_error
    }

    return render(request, 'proveedor/confi_inicial/contacto_ini_prov.html', context)



@login_required
def config_ini_ubicacion_prov(request):
    show_message_error = False
    
    try:
        profile = Profile_proveedor.objects.get(user=request.user)
        ubicacion = Ubicacion_proveedor.objects.get(user=profile)
    except Profile_proveedor.DoesNotExist:
        profile = None
        ubicacion = None
    except Ubicacion_proveedor.DoesNotExist:
        ubicacion = Ubicacion_proveedor(user=profile)
        ubicacion.save()

    if request.method == 'POST':
        provincia_prov = request.POST.get("provincias")
        ciudad_prov = request.POST.get("ciudad")
        calle_prov = request.POST.get("calle")
        num_loc_prov = request.POST.get("numero")

        if provincia_prov != None and ciudad_prov != None and calle_prov != None and num_loc_prov != None:

            ubicacion.provicia = provincia_prov
            ubicacion.ciudad = ciudad_prov
            ubicacion.calle = calle_prov
            ubicacion.numero = num_loc_prov
            ubicacion.save()

            return redirect('geo_servicios_prov')
        
        else:
            show_message_error = True
            return redirect('confini_ubicacion_prov')
        
    context = {
        'show_message_error': show_message_error
    }

    return render(request, 'proveedor/confi_inicial/config_ubicacion_inicial.html', context)




@login_required
def geo_servicios(request):
    show_message_error = False

    try:
        profile = Profile_proveedor.objects.get(user=request.user)
        area = Rango_servicio.objects.get(user=profile)
    except Profile_proveedor.DoesNotExist:
        profile = None
        area = None
    except Rango_servicio.DoesNotExist:
        area = Rango_servicio(user=profile)
        area.save()

    if request.method == 'POST':
        area_service = request.POST.get("geo_servicios")

        if area_service != None:
            area.geo_servicio = area_service
            area.save()

            return redirect('mensage_bienvenida_proveedor')

        else:

            show_message_error = True
            return redirect('geo_servicios_prov')

        
    
    context = {
        'show_message_error': show_message_error
        
    }

    return render(request, 'proveedor/confi_inicial/config_ini_geoservicio.html', context)




@login_required
def mensage_bienvenida_proveedor(request):

    return render(request, 'proveedor/confi_inicial/mensage_bienvenida_proveedor.html')

