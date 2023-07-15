from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate, login, logout
from django.core.mail import EmailMessage
from django.conf import settings
from django.utils.crypto import get_random_string
from .models import *
from django.core.exceptions import ValidationError
from django.core.mail import send_mail
from django.utils.crypto import get_random_string
from django.urls import reverse_lazy
from datetime import datetime, timedelta
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import random
from django.http import JsonResponse
from datetime import datetime
from datetime import date
from django.template.loader import render_to_string
from perfil_proveedor.models import Profile_proveedor
from login_vendedor.models import Profile_vendedor



def registro_proveedor(request):
    context = {}

    if request.user.is_authenticated:
        return redirect('comprueba_perfil')
    
    if request.method == 'POST':
        # obtenemos los datos del formulario
        nombre = request.POST['nombre']
        apellido = request.POST['apellido']
        usuario = request.POST['usuario']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        anio_nacimiento = int(request.POST['year'])
        mes_nacimiento = int(request.POST['month'])
        dia_nacimiento = int(request.POST['day'])

        
        # validamos que el usuario no exista
        if User.objects.filter(username=usuario).exists():
            posible_usuario = f"{usuario}{get_random_string(length=3)}"
            context['error_usuario'] = f'El usuario {usuario} ya existe. Prueba con {posible_usuario}'
            return render(request, 'proveedor/login_registro/registro.html', context=context)
        
        
        
        # validamos que el correo electrónico sea válido y no exista en la base de datos
        try:
            validate_email(email)
        except ValidationError:
            context['error_email'] = f'El correo electrónico es inválido.'
            return render(request, 'proveedor/login_registro/registro.html', context=context)
        if User.objects.filter(email=email).exists():
            context['error_email'] = f'El correo electrónico ya existe.'
            return render(request, 'proveedor/login_registro/registro.html', context=context)

        # validamos que las contraseñas sean iguales
        if password != password2:
            context['error_password'] = f'Las contraseñas no coinciden.'
            return render(request, 'proveedor/login_registro/registro.html', context=context)

        # validamos que el password cumpla con los requisitos mínimos
        if len(password) < 8 or not any(c.isupper() for c in password) or not any(c.islower() for c in password) or not any(c.isdigit() for c in password):
            context['error_password'] = f'El password debe tener al menos 8 caracteres, una mayúscula, una minúscula y un número.'
            return render(request, 'proveedor/login_registro/registro.html', context=context)
        
        # calculamos la edad del usuario a partir de su fecha de nacimiento
        hoy = date.today()
        edad = hoy.year - anio_nacimiento - ((hoy.month, hoy.day) < (mes_nacimiento, dia_nacimiento))

        # verificamos que el usuario tenga al menos 18 años
        if edad < 18:
            context['error_edad']= f'Debes tener al menos 18 años para registrarte como proveedor.'
            return render(request, 'proveedor/login_registro/registro.html', context=context)

      
        # creamos el usuario y su perfil
        user = User.objects.create_user(username=usuario, email=email, password=password)
        user.first_name = nombre
        user.last_name = apellido
        user.save()
        perfil = Profile_proveedor.objects.create(user=user)
        perfil.anio_nacimiento = anio_nacimiento
        perfil.mes_nacimiento = mes_nacimiento
        perfil.dia_nacimiento = dia_nacimiento
        perfil.save()

        # Envío del correo de confirmación
        send_confirmation_email(user)

        # iniciamos sesión en el usuario recién creado
        user = authenticate(username=usuario, password=password)
        login(request, user)

        return redirect('confirmar_proveedor')

    # si la petición es GET, mostramos el formulario de registro
    return render(request, 'proveedor/login_registro/registro.html', context=context)




def send_confirmation_email(user):
    # Generamos un código de confirmación
    codigo = str(random.randint(100000, 999999))
    confirmacion = Confirmacion(user=user, codigo=codigo)
    confirmacion.save()

    # Obtenemos el nombre y email del usuario
    nombre = user.first_name
    apellido = user.last_name
    email = user.email

    # Enviamos un correo de confirmación con el código
    subject = 'Confirmación de registro'
    message = f'Hola {nombre} {apellido}, gracias por registrarte en nuestro sitio. Por favor, introduce el siguiente código en la página de confirmación para activar tu cuenta: {codigo}'
    email = EmailMessage(subject, message, to=[email], from_email=settings.DEFAULT_FROM_EMAIL)
    email.send()





@login_required(login_url='registro_proveedor')
def confirmar_usuario(request):
    show_message_elert = False
    show_message_alert_codigo = False

    confirmacion = None

    if request.method == 'POST':
        codigo = request.POST['codigo']

        # validamos el código de confirmación
        try:
            confirmacion = Confirmacion.objects.get(codigo=codigo)
        except Confirmacion.DoesNotExist:

            show_message_alert_codigo = True


        if confirmacion: 
        # verificamos si el código ha caducado
            fecha_creacion = confirmacion.fecha_creacion
            fecha_actual = timezone.now()
            tiempo_expiracion = timedelta(minutes=10)

            if fecha_creacion + tiempo_expiracion < fecha_actual:
                confirmacion.delete()
                show_message_elert = True
            else:
                # activamos la cuenta del usuario y lo redirigimos a su perfil
                confirmacion.user.is_active = True
                confirmacion.user.save()
                login(request, confirmacion.user)
                confirmacion.delete()  # eliminamos el registro de ConfirmacionUsuario
                return redirect('bienvenida_proveedor')
    
    context = {
        'show_message_alert_codigo': show_message_alert_codigo,
        'show_message_elert_confimail': show_message_elert
    }
    #user.is_active = False # el usuario no puede iniciar sesión hasta confirmar su correo electrónico

    # si la petición es GET, mostramos la página de confirmación
    return render(request, 'proveedor/login_registro/confirmar_email_peoveedor.html', context)







@login_required
def enviar_nuevo_codigo(request):
    show_message_email = False
    if request.method == 'POST':
        # Eliminamos cualquier código de confirmación previo del usuario
        try:
            confirmacion_previa = Confirmacion.objects.get(user=request.user)
            confirmacion_previa.delete()
        except Confirmacion.DoesNotExist:
            pass

        # Generamos un nuevo código de confirmación
        codigo = str(random.randint(100000, 999999))
        confirmacion = Confirmacion(user=request.user, codigo=codigo)
        confirmacion.save()

        # Obtenemos el nombre y email del usuario
        nombre = request.user.first_name
        email = request.user.email

        # Enviamos el nuevo correo de confirmación con el código
        subject = 'Nuevo código de confirmación'
        message = f'Hola {nombre}, has solicitado un nuevo código de confirmación. Por favor, introduce el siguiente código en la página de confirmación para activar tu cuenta: {codigo}'
        email = EmailMessage(subject, message, to=[email], from_email=settings.DEFAULT_FROM_EMAIL)
        email.send()

        show_message_email = True
        
    contex = {
        'show_message_email_new_cod': show_message_email

    }

    return render(request, 'proveedor/login_registro/enviar_nuevo_codigo_proveedor.html', contex)







#//////////////////////// LOGIN Y LOGOUT //////////////////////////
def login_view(request):
    show_alert_login = False
    if request.user.is_authenticated:
        return redirect('comprueba_perfil')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('comprueba_perfil')
        else:
            show_alert_login = True

    context = {
        'show_alert': show_alert_login
    }
            
    return render(request, 'proveedor/login_registro/login.html', context)




@login_required
def logout_view(request):
    logout(request)
    return redirect('login_proveedor')








def recover_password(request):

    show_message_elert = False
    show_message_error = False

    if request.method == 'POST':
        email = request.POST['email']
        user = User.objects.filter(email=email).first()

        if user:
            # Genera una nueva contraseña aleatoria
            new_password = User.objects.make_random_password()
            user.set_password(new_password)
            user.save()

            # Envía un correo electrónico al usuario con la nueva contraseña
            subject = 'Nueva contraseña para su cuenta en Mi Sitio'
            body = render_to_string('proveedor/login_registro/new_password.html', {'username': user.username, 'password': new_password})
            email_message = EmailMessage(subject, body, 'noreply@misitio.com', [user.email])
            email_message.content_subtype = 'html'
            email_message.send()

            show_message_elert = True

            messages.success(request, 'Se ha enviado una nueva contraseña a su correo electrónico.')
            return redirect('login_proveedor')
        else:
            messages.error(request, 'No se encontró una cuenta con ese correo electrónico.')
            show_message_error = True

    context = {

        'show_message_elert': show_message_elert,
        'show_message_error': show_message_error,
        
    }
    
    return render(request, 'proveedor/login_registro/recoberi_password.html', context)




@login_required
def comprueba_perfil(request):
    if request.user.is_authenticated:
        user_profile = None
        if hasattr(request.user, 'profile_vendedor'):
            user_profile = request.user.profile_vendedor
            return redirect('vista_perfil_vend', codigo_unico_vend=user_profile.codigo_unico_vendedor)
        elif hasattr(request.user, 'profile_proveedor'):
            user_profile = request.user.profile_proveedor
            return redirect('vista_perfil_proveedor', codigo_unico=user_profile.codigo_unico_proveedor)
        else:
            return redirect('comprueba_perfil')
    else:
        return redirect('login_proveedor')
    






