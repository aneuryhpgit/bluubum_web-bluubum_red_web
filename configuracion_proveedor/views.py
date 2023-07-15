from django.shortcuts import render, redirect, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.conf import settings
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import update_session_auth_hash
# Create your views here.
from perfil_proveedor.models import Profile_proveedor
from config_inicial_prov.models import Contacto_proveedor, Ubicacion_proveedor, Rango_servicio

from storages.backends.gcloud import GoogleCloudStorage
from django.conf import settings




@login_required
def configuration_prov(request):
    return render(request, 'proveedor/menu/configuracion_prov.html')



@login_required
def edit_email_prov(request):
    user = User.objects.get(id=request.user.id)
    if request.method == 'POST':
        email = request.POST['email']
        user.email = email
        user.save()
        update_session_auth_hash(request, user)
        return redirect('edit_email_prov')
    
    context = {'email': user.email}
    return render(request, 'proveedor/editar_config/editar_email_prov.html', context)
    



@login_required
def edit_username_prov(request):
    user = request.user
    if request.method == 'POST':
        username = request.POST['username']
        user = User.objects.get(id=request.user.id)
        user.username = username
        user.save()
        update_session_auth_hash(request, user)
        return redirect('edit_username_prov')
    
    context = {'username': user}
    
    return render(request, 'proveedor/editar_config/editar_usuario_prov.html', context)
    


@login_required
def edit_password_prov(request):
    show_message_error = False
    user = User.objects.get(id=request.user.id)
    if request.method == 'POST':
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            user.set_password(password)
            user.plaintext_password = password 
            user.save()
            update_session_auth_hash(request, user)
            return redirect('edit_password_prov')
        else:
            show_message_error = True

    
    context = {'mesagge_error':show_message_error }
    return render(request, 'proveedor/editar_config/editar_password_prov.html', context)



#///////////////////////// EITAR PERFIL ////////////////////////////////////////
@login_required
def editar_perfil_prov(request):
    
    show_message_error = False
    show_message_exito = False
    profile = Profile_proveedor.objects.get_or_create(user=request.user.pk)[0]


    if request.method == 'POST':
        logo_edit = request.FILES.get("imagen-logo")
        nombreEmpresa = request.POST.get("nombre_empresa")

         # Asigna los valores existentes del modelo si no se proporcionan nuevos datos
        if logo_edit is None:
            logo_edit = profile.image
        if not nombreEmpresa:
            nombreEmpresa = profile.nombre_empresa

        # Actualiza los campos del modelo si se proporcionan nuevos datos
        if logo_edit != profile.image or nombreEmpresa.strip() != profile.nombre_empresa:
            
            if logo_edit:
                image_logo_path = f'{settings.PUBLIC_MEDIA_LOCATION}/{logo_edit.name}'
                storage = GoogleCloudStorage()
                storage.save(image_logo_path, logo_edit)
                profile.image = image_logo_path

            

            profile.nombre_empresa = nombreEmpresa
            profile.save()
            
            show_message_exito = True
        else:
            show_message_error = True
            
            
    
    context = {
        'show_message_error': show_message_error,
        'show_message_exito': show_message_exito,
        'profile': profile,
    }

    return render(request, 'proveedor/editar_config/editar_perfil_prov.html', context)




#/////////////////////////////// EDITAR CONTACTO /////////////////////////////////////
@login_required
def editar_contacto_prov(request):
    
    show_message_error = False
    show_message_exito = False
    contacto = Contacto_proveedor.objects.get_or_create(user=request.user.pk)[0]


    if request.method == 'POST':
        numero_whatsapp = request.POST.get("numero_whatsapp")
        numero_telefono = request.POST.get("numero_telefono")

         # Asigna los valores existentes del modelo si no se proporcionan nuevos datos
        if not numero_whatsapp:
            numero_whatsapp = contacto.numWhatsapp
        if not numero_telefono:
            numero_telefono = contacto.telefono

        # Actualiza los campos del modelo si se proporcionan nuevos datos
        if numero_whatsapp.strip() != contacto.numWhatsapp or numero_telefono.strip() != contacto.telefono:
            contacto.numWhatsapp = numero_whatsapp.strip()
            contacto.telefono = numero_telefono.strip()
            contacto.save()
            show_message_exito = True
        else:
            show_message_error = True
            
            
    context = {
        'show_message_error': show_message_error,
        'show_message_exito': show_message_exito,
        'contacto': contacto,
    }

    return render(request, 'proveedor/editar_config/editar_contacto_prov.html', context)




#/////////////////////////////// EDITAR UBICACION /////////////////////////////////////
@login_required
def editar_ubicacion_prov(request):
    
    show_message_error = False
    show_message_exito = False
    direccion = Ubicacion_proveedor.objects.get_or_create(user=request.user.pk)[0]
    

    if request.method == 'POST':
        provincia = request.POST.get("provincias")
        ciudad = request.POST.get("ciudad")
        calle = request.POST.get("calle")
        numero = request.POST.get("numero")

         # Asigna los valores existentes del modelo si no se proporcionan nuevos datos
        if provincia is None:
            provincia = direccion.provicia
        if not ciudad:
            ciudad = direccion.ciudad
        if not calle:
            calle = direccion.calle
        if not numero:
            numero = direccion.numero

        # Actualiza los campos del modelo si se proporcionan nuevos datos
        if provincia.strip() != direccion.provicia or ciudad.strip() != direccion.ciudad or calle.strip() != direccion.calle or numero.strip() != direccion.numero:
            direccion.provicia = provincia.strip()
            direccion.ciudad = ciudad.strip()
            direccion.calle = calle.strip()
            direccion.numero = numero.strip()
            direccion.save()
            show_message_exito = True
        else:
            show_message_error = True
            
            
    context = {
        'show_message_error': show_message_error,
        'show_message_exito': show_message_exito,
        'direccion': direccion,
    }

    return render(request, 'proveedor/editar_config/editar_ubicacion_prov.html', context)




#/////////////////////////////// EDITAR GEO-SERVICIOS //////////////////////////////////
@login_required
def editar_geo_prov(request):
    
    show_message_error = False
    show_message_exito = False
    geo = Rango_servicio.objects.get_or_create(user=request.user.pk)[0]


    if request.method == 'POST':
        geoServicio = request.POST.get("geo_servicios")

         # Asigna los valores existentes del modelo si no se proporcionan nuevos datos
        if geoServicio is None:
            geoServicio = geo.geo_servicio

        # Actualiza los campos del modelo si se proporcionan nuevos datos
        if geoServicio.strip() != geo.geo_servicio:
            geo.geo_servicio = geoServicio.strip()
            geo.save()
            show_message_exito = True
        else:
            show_message_error = True
            
            
    context = {
        'show_message_error': show_message_error,
        'show_message_exito': show_message_exito,
        'geo': geo,
    }

    return render(request, 'proveedor/editar_config/editar_geoservicio_prov.html', context)













