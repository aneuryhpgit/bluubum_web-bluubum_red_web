from django.shortcuts import render
from .models import PaginaPrincipal, Imagen_itileria, Politicas, Message
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from perfil_proveedor.models import Profile_proveedor
from login_vendedor.models import Profile_vendedor



# Create your views here.


def error_404(request, exception):
    return render(request, '404/404.html', status=404)



def home_page(request):

    if request.user.is_authenticated:
        user_profile = None
        if hasattr(request.user, 'profile_vendedor'):
            user_profile = request.user.profile_vendedor
            return redirect('vista_perfil_vend', codigo_unico_vend=user_profile.codigo_unico_vendedor)
        elif hasattr(request.user, 'profile_proveedor'):
            user_profile = request.user.profile_proveedor
            return redirect('vista_perfil_proveedor', codigo_unico=user_profile.codigo_unico_proveedor)

    image_banner = Imagen_itileria.objects.all()

    context = {
        'image_banner': image_banner,
    }

    return render(request, 'home/home.html', context)






#politica de privacidad de usuarios vendedore

def politicas_privacidad_user_vend(request):

    text_politica = Politicas.objects.filter(titulo='politica')

    context = {'text_politica': text_politica}

    return render(request, 'home/politica_user_vend.html', context)




#Terminos y condiciones de usurios vendedor 
def terminos_user_vend(request):
    
    text_termino = Politicas.objects.filter(titulo='terminos')

    context = {'text_termino': text_termino}

    return render(request, 'home/terminos_vendedor.html', context)



#mensage de contactar
def message_form(request):
    if request.method == 'POST':
        sender_name = request.POST.get('sender_name')
        sender_email = request.POST.get('sender_email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        Message.objects.create(
            sender_name=sender_name,
            sender_email=sender_email,
            subject=subject,
            message=message
        )

        return redirect('success')  # Redirigir a una página de éxito o agradecimiento

    return render(request, 'home/mensage_contacto.html')




def message_list(request):
    messages = Message.objects.all()
    return render(request, 'message_list.html', 
        {'messages': messages}
    )







# VISTAS DE ERRORES
def custom_400_view(request, exception):
    return render(request, 'templates/404/400.html', status=400)
"""
def custom_401_view(request, exception):
    return render(request, 'templates/404/401.html', status=401)
"""
def custom_403_view(request, exception):
    return render(request, 'templates/404/403.html', status=403)

def custom_404_view(request):
    return render(request, '404/405.html', status=404)
"""
def custom_405_view(request, exception):
    return render(request, 'templates/404/405.html', status=405)

def custom_408_view(request, exception):
    return render(request, 'templates/404/408.html', status=408)
"""
def custom_500_view(request):
    return render(request, 'templates/404/500.html', status=500)
"""
def custom_502_view(request, exception):
    return render(request, 'templates/404/502.html', status=502)

def custom_503_view(request, exception):
    return render(request, 'templates/404/503.html', status=503)
"""