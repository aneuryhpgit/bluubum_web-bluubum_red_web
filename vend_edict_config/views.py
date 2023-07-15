from django.shortcuts import render, redirect
from django.utils import timezone
from datetime import timedelta
from django.contrib.auth import update_session_auth_hash, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from login_vendedor.models import Profile_vendedor
from vend_config_inic.models import Contacto_vendedor, Direccion_vendedor, Metodo_pago_vendedor
from perfil_proveedor.models import Confirmacion
import random
from django.core.mail import EmailMessage
from django.conf import settings
from .models import *

from storages.backends.gcloud import GoogleCloudStorage
from django.conf import settings



# Resto del código de tu aplicación

# Create your views here.




@login_required(login_url='login_vnd')
def configuracion_vend(request):

    return render(request, 'vendedor/menu/configuracion_vend.html')


@login_required(login_url='login_vnd')
def edit_email_vend(request):
    mesage_alert_exist = False
    mesage_alert_aprobado = False
    user = request.user


    try:   
        tmpe = Email_temporal.objects.get(user=user)
    except Email_temporal.DoesNotExist:            
        tmpe = None

    if request.method == 'POST':
        new_email = request.POST['email']

        # Verificar si el nuevo correo electrónico ya existe en la base de datos
        if User.objects.filter(email=new_email).exists():
            mesage_alert_exist = True
            
        elif not User.objects.filter(email=new_email).exists():
            codigo = str(random.randint(100000, 999999))
            # Guardamos el nuevo email en una variable temporal
            if tmpe is None:
                tmpe = Email_temporal(user=user, email_temp=new_email)
            else:
                tmpe.email_temp = new_email
            tmpe.save()
            # Enviamos un correo de confirmación con el código
            send_confirmation_email_vend(user, codigo)
            
            codigo = str(random.randint(100000, 999999))
        
            # Guardamos el nuevo email en una variable temporal
            if tmpe is None:
                tmpe = Email_temporal(user=user, email_temp=new_email)
            else:
                tmpe.email_temp = new_email
            tmpe.save()
            # Enviamos un correo de confirmación con el código
            send_confirmation_email_vend(user, codigo)
        

            # Actualizamos el contexto para mostrar un mensaje al usuario
            mesage_alert_aprobado = True
    
    context = {'user': user, 'tmpe': tmpe, 'mesage_alert_exist': mesage_alert_exist, 'mesage_alert': mesage_alert_aprobado}
    return render(request, 'vendedor/edict_config/editar_email_vend.html', context)




def send_confirmation_email_vend(user, codigo):
    # Creamos un registro de confirmación con el código generado
    tmpe = Email_temporal.objects.get(user=user)
    confirmacion = Confirmacion(user=user, codigo=codigo)
    confirmacion.save()

    # Obtenemos el nombre y email del usuario
    nombre = user.first_name
    apellido = user.last_name
    email = tmpe.email_temp

    # Enviamos un correo de confirmación con el código
    subject = 'Confirmación de cambio de correo electrónico'
    message = f'Hola {nombre} {apellido}, has solicitado cambiar tu correo electrónico en nuestro sitio. Por favor, introduce el siguiente código en la página de confirmación para confirmar el cambio: {codigo}'
    email = EmailMessage(subject, message, to=[email], from_email=settings.DEFAULT_FROM_EMAIL)
    email.send()



@login_required(login_url='login_vnd')
def confirmar_cambio_email_vend(request):

    show_message_invalid = False
    show_message_caducad = False
    show_message_exitoso = False
    
    user = request.user
    tmpe = Email_temporal.objects.filter(user=user).first()
    
    confirmacion = None #inicializamos la variable confirmacion

    if request.method == 'POST':
        codigo = request.POST['codigo']

        # Validamos el código de confirmación
        try:
            confirmacion = Confirmacion.objects.get(codigo=codigo)
        except Confirmacion.DoesNotExist:
            show_message_invalid = True

        # validamos el código de confirmación
        if confirmacion: 
            # Verificamos si el código ha caducado
            fecha_creacion = confirmacion.fecha_creacion
            fecha_actual = timezone.now()
            tiempo_expiracion = timedelta(minutes=10)

            if fecha_creacion + tiempo_expiracion < fecha_actual:
                confirmacion.delete()
                show_message_caducad = True

            else:
                # Actualizamos el email del usuario y lo redirigimos a su perfil
                user = confirmacion.user
                user.email = tmpe.email_temp
                user.email_temp = ''
                user.save()
                login(request, user)
                confirmacion.delete()
                tmpe.delete()
                show_message_exitoso = True
        
    
    context = {
        'show_message_invalid': show_message_invalid,
        'show_message_caducad': show_message_caducad,
        'show_message_exitoso': show_message_exitoso,
    }
    
    return render(request, 'vendedor/edict_config/confirma_codigo_new_email.html', context)





#////////////////////////////// EDITAR NOMBRE USUARIO ///////////////////////////
@login_required(login_url='login_vnd')
def edit_username_vend(request):

    show_message_alert = False
    show_message_error = False

    user = request.user
    if request.method == 'POST':
        username = request.POST['username']
        # Verificar si el usuario ya existe
        if User.objects.filter(username=username).exists():
            show_message_error = True
            
        elif not User.objects.filter(username=username).exists():    
            user.username = username
            user.save()
            update_session_auth_hash(request, user)
            show_message_alert = True

    context = {
        'user': user,
        'show_message_alert': show_message_alert,
        'show_message_error': show_message_error,
    }
    
    return render(request, 'vendedor/edict_config/editar_usuario_vend.html', context)



#/////////////////////////////////// EDITAR PASSWORD ///////////////////////////
@login_required(login_url='login_vnd')
def edit_password_vend(request):
    show_message_error_password_diferent = False
    show_message_clave_incumple = False
    show_message_clave_actualizada = False

    user = User.objects.get(id=request.user.id)
    if request.method == 'POST':
        password = request.POST['password']
        password2 = request.POST['password2']

        # validamos que las contraseñas sean iguales
        if password != password2:
            show_message_error_password_diferent = True

        if password == password2:
            # validamos que el password cumpla con los requisitos mínimos
            if len(password) < 8 or not any(c.isupper() for c in password) or not any(c.islower() for c in password) or not any(c.isdigit() for c in password):
                show_message_clave_incumple = True

            else:
                user.set_password(password)
                user.plaintext_password = password 
                user.save()
                update_session_auth_hash(request, user)

                show_message_clave_actualizada = True

    context = {
        'show_message_error_password_diferent': show_message_error_password_diferent, 
        'show_message_clave_incumple': show_message_clave_incumple,
        'show_message_clave_actualizada': show_message_clave_actualizada,
    }
    return render(request, 'vendedor/edict_config/editar_password_vend.html', context)




#///////////////////////// EITAR PERFIL ////////////////////////////////////////
@login_required(login_url='login_vnd')
def editar_foto_perfil_vend(request):
    
    show_message_error = False
    show_message_exito = False

    profile = Profile_vendedor.objects.get_or_create(user=request.user.pk)[0]

    if request.method == 'POST':
        logo = request.FILES.get("imagen-logo")

         # Asigna los valores existentes del modelo si no se proporcionan nuevos datos
        if logo is None:
            logo = profile.image

        # Actualiza los campos del modelo si se proporcionan nuevos datos
        if logo != profile.image:

            image_logo_path = f'{settings.PUBLIC_MEDIA_LOCATION}/{logo.name}'
            storage = GoogleCloudStorage()
            storage.save(image_logo_path, logo)
            profile.image = image_logo_path

            profile.save()
            show_message_exito = True
        else:
            show_message_error = True
            
    context = {
        'show_message_error': show_message_error,
        'show_message_exito': show_message_exito,
        'profile': profile,
    }

    return render(request, 'vendedor/edict_config/editar_foto_perfil.html', context)



#/////////////////////////////// EDITAR CONTACTO /////////////////////////////////////
@login_required(login_url='login_vnd')
def editar_contacto_vend(request):
    
    show_message_error = False
    show_message_exito = False
    contacto = Contacto_vendedor.objects.get_or_create(user=request.user.profile_vendedor)[0]


    if request.method == 'POST':
        numero_whatsapp = request.POST.get("numero_whatsapp")
        numero_telefono = request.POST.get("numero_telefono")

         # Asigna los valores existentes del modelo si no se proporcionan nuevos datos
        if numero_whatsapp is None:
            numero_whatsapp = contacto.numeroWhatsapp_afiliado
        if not numero_telefono:
            numero_telefono = contacto.telefono

        # Actualiza los campos del modelo si se proporcionan nuevos datos
        if numero_whatsapp.strip() != contacto.numeroWhatsapp_afiliado or numero_telefono.strip() != contacto.telefono:
            contacto.numeroWhatsapp_afiliado = numero_whatsapp.strip()
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

    return render(request, 'vendedor/edict_config/edict_contac_vend.html', context)




#/////////////////////////////// EDITAR UBICACION /////////////////////////////////////
@login_required(login_url='login_vnd')
def editar_ubicacion_vend(request):
    
    show_message_error = False
    show_message_exito = False

    direccion = Direccion_vendedor.objects.get_or_create(user=request.user.profile_vendedor)[0]
    
    if request.method == 'POST':
        provincia_vend = request.POST.get("provincias")
        ciudad_vend = request.POST.get("ciudad")
        sector_vend = request.POST.get("sector")
        calle_vend = request.POST.get("calle")
        num_loc_vend = request.POST.get("numero")
        partamento_suite_vend = request.POST.get("apartamento_num")

         # Asigna los valores existentes del modelo si no se proporcionan nuevos datos
        if not provincia_vend:
            provincia_vend = direccion.provincia_afiliado
        if not ciudad_vend:
            ciudad_vend = direccion.ciudad_afiliado
        if not sector_vend:
            sector_vend = direccion.sector_afiliado
        if not calle_vend:
            calle_vend = direccion.calle_afiliado
        if not num_loc_vend:
            num_loc_vend = direccion.numero
        if not partamento_suite_vend:
            partamento_suite_vend = direccion.apartamento_num
        

        # Actualiza los campos del modelo si se proporcionan nuevos datos
        if provincia_vend.strip() != direccion.provincia_afiliado or ciudad_vend.strip() != direccion.ciudad_afiliado or sector_vend.strip() != direccion.sector_afiliado or calle_vend.strip() != direccion.calle_afiliado or num_loc_vend.strip() != direccion.numero or partamento_suite_vend.strip() != direccion.apartamento_num:

            direccion.provincia_afiliado = provincia_vend.strip()
            direccion.ciudad_afiliado = ciudad_vend.strip()
            direccion.sector_afiliado = sector_vend.strip()
            direccion.calle_afiliado = calle_vend.strip()
            direccion.numero = num_loc_vend.strip()
            direccion.apartamento_num = partamento_suite_vend.strip()
            direccion.save()
            show_message_exito = True
        else:
            show_message_error = True
            
            
    context = {
        'show_message_error': show_message_error,
        'show_message_exito': show_message_exito,
        'direccion': direccion,
    }

    return render(request, 'vendedor/edict_config/edict_direc_vend.html', context)





#/////////////////////////// EDITAR METODO DE PAGO ////////////////////////
@login_required(login_url='login_vnd')
def metodo_pago_edict_vend(request):
    show_message_exitoso = False
    show_message_error = False

    mtd = Metodo_pago_vendedor.objects.get_or_create(user=request.user.profile_vendedor)[0]

    if request.method == 'POST':
        met_pago = request.POST.get("metodo_pago")
        tipo_document = request.POST.get("tipo_documet")
        nombre_idp = request.POST.get("nombre_idp")
        nombre_banco = request.POST.get("nombre_banco")
        numero_cuenta = request.POST.get("numero_cuenta")


        if met_pago.strip() == "Depósito de efectivo":
            mtd.nombre_banco = ''
            mtd.Numero_cuenta_bancaria = ''
            mtd.delete()



        if not met_pago: 
            met_pago = mtd.metodo_cobro  
        if not tipo_document:
            tipo_document = mtd.tipo_document_identificacion
        if not nombre_idp:
            nombre_idp = mtd.Nombre_completo_identificacion
        if not nombre_banco:
            nombre_banco = mtd.nombre_banco
        if not numero_cuenta:
            numero_cuenta = mtd.Numero_cuenta_bancaria


        

        if met_pago.strip() != mtd.metodo_cobro or tipo_document.strip() != mtd.tipo_document_identificacion or nombre_idp.strip() != mtd.Nombre_completo_identificacion or nombre_banco.strip() != mtd.nombre_banco or numero_cuenta.strip() != mtd.Numero_cuenta_bancaria:

            
            mtd.metodo_cobro = met_pago.strip()
            mtd.tipo_document_identificacion = tipo_document.strip()
            mtd.Nombre_completo_identificacion = nombre_idp.strip()
            mtd.nombre_banco = nombre_banco.strip()
            mtd.Numero_cuenta_bancaria = numero_cuenta.strip()
            mtd.save()
            show_message_exitoso = True

        
        else:
            show_message_error = True
        
    context = {
        'mtd': mtd,
        'show_message_exitoso': show_message_exitoso,
        'show_message_error': show_message_error,
    }

    return render(request, 'vendedor/edict_config/edict_metod_pago.html', context)



