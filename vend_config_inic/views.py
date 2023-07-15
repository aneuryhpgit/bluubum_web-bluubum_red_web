from django.shortcuts import render, redirect
from .models import *
from login_vendedor.models import Profile_vendedor
from django.contrib.auth.decorators import login_required

from storages.backends.gcloud import GoogleCloudStorage
from django.conf import settings
# Create your views here.



#BIENVENIDA
@login_required(login_url='login_vnd')
def bienvenida_vendedor(request):
    
    return render(request, 'vendedor/config_inic_vend/bienvenida_vend.html')



#SUBE LA FOTO DE PEFIL DEL VENDEDO
@login_required(login_url='login_vnd')
def foto_vendedor(request):
    show_message_error = False
    
    #verifica que exista el perfil y si no es asi crea uno
    try:
        profile = Profile_vendedor.objects.get(user=request.user)
    except Profile_vendedor.DoesNotExist:
        profile = Profile_vendedor.objects.create(user=request.user)

    #mediante el metodo post se rescata la informacion del input
    if request.method == 'POST':
        logo = request.FILES.get("imagen-logo")

        #verifica si la informacion del input no esta basia  
        if logo != None:
            #guara la imagen en una carpeta en el buke de google storage
            image_logo_path = f'{settings.PUBLIC_MEDIA_LOCATION}/{logo.name}'
            storage = GoogleCloudStorage()
            storage.save(image_logo_path, logo)
            profile.image = image_logo_path
            
            profile.save()

            return redirect('config_ini_contacto_vendedor')
        
        else:
            show_message_error = True
            return redirect('foto_vendedor')
        
    context = {
        'show_message_error': show_message_error
    }


    return render(request, 'vendedor/config_inic_vend/imagen_perfil_vend.html', context)



#GUARDA LOS DATOS DE CONTACTO DEL VENDEDOR WHATSAPP Y NUMERO TELEFONO
@login_required(login_url='login_vnd')
def config_ini_contacto_vend(request):
    show_message_error = False

    try:
        profile = Profile_vendedor.objects.get(user=request.user)
        contacto = Contacto_vendedor.objects.get(user=profile)
    except Profile_vendedor.DoesNotExist:
        profile = None
        contacto = None
    except Contacto_vendedor.DoesNotExist:
        contacto = Contacto_vendedor(user=profile)
        contacto.save()

    if request.method == 'POST':    
        numero_whatsapp = request.POST.get("numero_whatsapp")
        numero_telefono = request.POST.get("numero_telefono")

        if numero_whatsapp != None and numero_telefono != None:
            
            contacto.numeroWhatsapp_afiliado = numero_whatsapp
            contacto.telefono = numero_telefono
            contacto.save()

            return redirect('config_ini_ubicacion_vend')
        
        else:
            show_message_error = True
            return redirect('config_ini_contacto_vendedor')
        
    context = {
        'show_message_error': show_message_error
    }

    return render(request, 'vendedor/config_inic_vend/contacto_vendedor.html', context)





#GUARDA LA DIRECCION DEL VENDEDOR
@login_required(login_url='login_vnd')
def config_ini_ubicacion_vend(request):
    show_message_error = False

    try:
        profile = Profile_vendedor.objects.get(user=request.user)
        ubicacion = Direccion_vendedor.objects.get(user=profile)
    except Profile_vendedor.DoesNotExist:
        profile = None
        ubicacion = None
    except Direccion_vendedor.DoesNotExist:
        ubicacion = Direccion_vendedor(user=profile)
        ubicacion.save()

    if request.method == 'POST':
        provincia_prov = request.POST.get("provincias")
        ciudad_prov = request.POST.get("ciudad")
        sector = request.POST.get("sector")
        calle_prov = request.POST.get("calle")
        num_loc_prov = request.POST.get("numero")
        partamento_suite = request.POST.get("apartamento_num")

        if provincia_prov != None and ciudad_prov != None and sector != None and calle_prov != None and num_loc_prov != None:

            ubicacion.provincia_afiliado = provincia_prov
            ubicacion.ciudad_afiliado = ciudad_prov
            ubicacion.sector_afiliado = sector
            ubicacion.calle_afiliado = calle_prov
            ubicacion.numero = num_loc_prov
            ubicacion.apartamento_num = partamento_suite
            ubicacion.save()

            return redirect('metodo_pago_inic_vend')
        
        else:
            show_message_error = True
            return redirect('config_ini_ubicacion_vend')
        
    context = {
        'show_message_error': show_message_error
    }

    return render(request, 'vendedor/config_inic_vend/direccion_inic_vend.html', context)



#GUARDA LA INFORMACION DE PAGO DEL VENDEDOR
@login_required(login_url='login_vnd')
def metodo_pago_inic_vend(request):
    show_message_error = False

    try:
        profile = Profile_vendedor.objects.get(user=request.user)
        mtd = Metodo_pago_vendedor.objects.get(user=profile)
    except Profile_vendedor.DoesNotExist:
        profile = None
        mtd = None
    except Metodo_pago_vendedor.DoesNotExist:
        mtd = Metodo_pago_vendedor(user=profile)
        mtd.save()

    if request.method == 'POST':
        met_pago = request.POST.get("metodo_pago")
        tipo_document = request.POST.get("tipo_documet")
        nombre_idp = request.POST.get("nombre_idp")
        nombre_banco = request.POST.get("nombre_banco")
        numero_cuenta = request.POST.get("numero_cuenta")


        if met_pago != None and tipo_document != None and nombre_idp != None:

            mtd.metodo_cobro = met_pago
            mtd.tipo_document_identificacion = tipo_document
            mtd.Nombre_completo_identificacion = nombre_idp
            mtd.nombre_banco = nombre_banco
            mtd.Numero_cuenta_bancaria = numero_cuenta
            mtd.save()

            return redirect('info_inic_vend')
        
        else:
            show_message_error = True
            return redirect('metodo_pago_inic_vend')
        
    context = {
        'show_message_error': show_message_error
    }

    return render(request, 'vendedor/config_inic_vend/datos_metodo_pago.html', context)



#GUARADA TRUE EN LA COLUMMNA DE DB CONFIG PARA ESTABLECER QUE HA SIDO CONFIGURADO LA INFORMACION INICIAL DEL VENDEDOR
@login_required(login_url='login_vnd')
def info_inic_vend(request):

        try:
           profile = Profile_vendedor.objects.get(user=request.user)
        except Profile_vendedor.DoesNotExist:
            profile = Profile_vendedor.objects.create(user=request.user)
            profile.configured = False
            profile.save()
        
        if profile:
            if request.method == 'POST':
               profile.configured = True  
               profile.save()

               return redirect('comprueba_perfil_vend')
        
        return render(request, 'vendedor/config_inic_vend/info_bienvenida_vend.html')




def info_bienvenida_dos_vend(request):

    return render(request, 'vendedor/config_inic_vend/info_bienvenida_dos_vend.html')