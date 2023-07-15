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
from perfil_proveedor.models import Confirmacion
from django.core.mail import EmailMessage
# Create your views here.



def registro_vendedor(request):

    context = {}

    if request.user.is_authenticated:
        return redirect('comprueba_perfil_vend')
    
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
            return render(request, 'vendedor/login_registro/registro_vend.html', context=context)
           
            
        # validamos que el correo electrónico sea válido y no exista en la base de datos
        try:
            validate_email(email)
        except ValidationError:
            context['error_email'] = f'El correo electrónico es inválido.'
            return render(request, 'vendedor/login_registro/registro_vend.html', context=context)
    
        if User.objects.filter(email=email).exists():
            context['error_email'] = f'El correo electrónico ya existe.'
            return render(request, 'vendedor/login_registro/registro_vend.html', context=context)

        # validamos que las contraseñas sean iguales
        if password != password2:
            context['error_password'] = f'Las contraseñas no coinciden.'
            return render(request, 'vendedor/login_registro/registro_vend.html', context=context)

        # validamos que el password cumpla con los requisitos mínimos
        if len(password) < 8 or not any(c.isupper() for c in password) or not any(c.islower() for c in password) or not any(c.isdigit() for c in password):
            context['error_password'] = f'El password debe tener al menos 8 caracteres, una mayúscula, una minúscula y un número.'
            return render(request, 'vendedor/login_registro/registro_vend.html', context=context)
        
        # calculamos la edad del usuario a partir de su fecha de nacimiento
        hoy = date.today()
        edad = hoy.year - anio_nacimiento - ((hoy.month, hoy.day) < (mes_nacimiento, dia_nacimiento))

        # verificamos que el usuario tenga al menos 18 años
        if edad < 18:
            context['error_edad']= f'Debes tener al menos 18 años para registrarte como vendedor.'
            return render(request, 'vendedor/login_registro/registro_vend.html', context)

      
        # creamos el usuario y su perfil
        user = User.objects.create_user(username=usuario, email=email, password=password)
        user.first_name = nombre
        user.last_name = apellido
        user.save()
        perfil = Profile_vendedor.objects.create(user=user)
        perfil.anio_nacimiento = anio_nacimiento
        perfil.mes_nacimiento = mes_nacimiento
        perfil.dia_nacimiento = dia_nacimiento
        perfil.save()

        # Envío del correo de confirmación
        send_confirmation_email(user)

        # iniciamos sesión en el usuario recién creado
        user = authenticate(username=usuario, password=password)
        login(request, user)

        return redirect('confirmar_usuario_vend')


    # si la petición es GET, mostramos el formulario de registro
    return render(request, 'vendedor/login_registro/registro_vend.html', context=context)



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
    # Estilos en línea para el mensaje de correo electrónico
    estilos = """
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f3f3f3;
            padding: 20px;
        }
        
        .container {
            background-color: #ffffff;
            max-width: 600px;
            margin: 0 auto;
            padding: 20px;
            border-radius: 5px;
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
        }
        
        h1 {
            color: #007bff;
        }
        
        p {
            margin-bottom: 20px;
        }
        
        .code {
            background-color: #f9f9f9;
            padding: 10px;
            border-radius: 5px;
            font-size: 18px;
        }
    </style>
    """

    # Contenido del mensaje con estilos en línea
    message = f"""
        <html>
        <head>
            {estilos}
        </head>
        <body>
            <div class="container">
                <h1>Confirmación de registro Bluubum</h1>
                <p>Hola {nombre} {apellido}, gracias por registrarte en nuestro sitio. Por favor, introduce el siguiente código en la página de confirmación para activar tu cuenta:</p>
                <p class="code">{codigo}</p>
            </div>
        </body>
        </html>
    """

    # Envío del correo electrónico
    subject = 'Confirmación de registro Bluubum'
    from_email = settings.DEFAULT_FROM_EMAIL
    to_email = [email]

    email = EmailMessage(subject, message, from_email, to_email)
    email.content_subtype = 'html'  # Indicar que el contenido es HTML

    # Enviar el correo electrónico
    email.send()

    #subject = 'Confirmación de registro Bluubum'
    #message = f'Hola {nombre} {apellido}, gracias por registrarte en nuestro sitio. Por favor, introduce el siguiente código en la página de confirmación para activar tu cuenta: {codigo}'
    #email = EmailMessage(subject, message, to=[email], from_email=settings.DEFAULT_FROM_EMAIL)
    #email.send()




@login_required(login_url='registro_vendedor')
def confirmar_usuario_vend(request):

    show_alert = False
    show_message_alert_caduca = False

    confirmacion = None
    
    if request.method == 'POST':
        codigo = request.POST['codigo']

        try:
            confirmacion = Confirmacion.objects.get(codigo=codigo)
        except Confirmacion.DoesNotExist:
            show_alert = True

        if confirmacion:
            fecha_creacion = confirmacion.fecha_creacion
            fecha_actual = timezone.now()
            tiempo_expiracion = timedelta(minutes=10)

            if fecha_creacion + tiempo_expiracion < fecha_actual:
                confirmacion.delete()
                show_message_alert_caduca = True

            else:
                confirmacion.user.is_active = True
                confirmacion.user.save()
                confirmacion.confirmado = True  # Marcar confirmado como True en el registro de confirmación
                confirmacion.save()
                login(request, confirmacion.user)
                return redirect('bienvenida_vendedor')

    context = {
        'show_alert': show_alert,
        'show_message_alert_caduca': show_message_alert_caduca,
    }

    return render(request, 'vendedor/login_registro/confirmar_email_vendedor.html', context)





@login_required
def enviar_nuevo_codigo_vendedor(request):

    show_message_alert = False

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
        subject = 'Nuevo código de confirmación Bluubum'
        message = f'Hola {nombre}, has solicitado un nuevo código de confirmación. Por favor, introduce el siguiente código en la página de confirmación para activar tu cuenta: {codigo}'
        email = EmailMessage(subject, message, to=[email], from_email=settings.DEFAULT_FROM_EMAIL)
        email.send()

        show_message_alert = True
        
    
    context = {
        'show_message_alert': show_message_alert
    }
    return render(request, 'vendedor/login_registro/nuevo_codigo_vendedor.html', context)





#//////////////////////// LOGIN Y LOGOUT //////////////////////////
def login_vendedor(request):

    show_alert_login = False

    if request.user.is_authenticated:
        return redirect('comprueba_perfil_vend')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('comprueba_perfil_vend')
        else:
            show_alert_login = True

    context = {
        'show_alert_login': show_alert_login
    }
            
    return render(request, 'vendedor/login_registro/login_vendedor.html', context)




@login_required
def logout_vendedor(request):
    logout(request)
    return redirect('login_vnd')



def restaurar_password(request):
    alerta_user = False
    show_message_alert = False
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
            subject = 'Nueva contraseña para su cuenta en Bluubum'
            body = render_to_string('vendedor/login_registro/nuevo_password.html', {'username': user.username, 'password': new_password})
            email_message = EmailMessage(subject, body, 'noreply@bluubum.com', [user.email])
            email_message.content_subtype = 'html'
            email_message.send()
            
            alerta_user = True
            show_message_alert = True
        else:
            show_message_error = True


    context = {
        'alerta_user': alerta_user,
        'show_message_alert': show_message_alert,
        'show_message_error': show_message_error,
    }
    
    return render(request, 'vendedor/login_registro/recobrar_password.html', context)




@login_required
def comprueba_perfil_vend(request):
    if request.user.is_authenticated:
        user_profile = None
        if hasattr(request.user, 'profile_vendedor'):
            user_profile = request.user.profile_vendedor
            return redirect('vista_perfil_vend', codigo_unico_vend=user_profile.codigo_unico_vendedor)
        elif hasattr(request.user, 'profile_proveedor'):
            user_profile = request.user.profile_proveedor
            return redirect('vista_perfil_proveedor', codigo_unico=user_profile.codigo_unico_proveedor)
        else:
            return redirect('comprueba_perfil_vend')
    else:
        return redirect('login_vnd')
    



def perfil_vendedor(request):
    if not request.user.is_authenticated:
        return redirect('login_vnd')

    return render(request, 'vendedor/login_registro/perfil_vendedor.html')