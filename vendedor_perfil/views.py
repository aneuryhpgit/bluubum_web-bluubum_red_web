from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from login_vendedor.models import Profile_vendedor
from prov_servis.models import Servicio_prov
from dashboard_prov.models import Afiliacion
from dashboard_prov.models import CrearProyecto, Comisiones_vendedor
from perfil_proveedor.models import Profile_proveedor
from django.utils import timezone
from datetime import datetime, timedelta
from .models import Duda_comentario
from vend_config_inic.models import Contacto_vendedor
from django.db.models.functions import Random


@login_required(login_url='login_vnd')
def vista_lista_proveedor(request):

    user = request.user
    profile = Profile_vendedor.objects.get(user=user)
    
    proveedorVis = Profile_proveedor.objects.all().order_by(Random())
    
    servicios = Servicio_prov.objects.filter(user__in=proveedorVis)

    context = {
        'profile': profile,
       
        'proveedorVis': proveedorVis,

        'servicios': servicios,
    }

    return render(request, 'vendedor/dashboard_vend/vista_lista_prov.html', context)




@login_required(login_url='login_vnd')
def proveedores_afiliados(request, vendedor_id):
    user = request.user
    profile = Profile_vendedor.objects.get(user=user)
    afiliaciones = Afiliacion.objects.filter(vendedor_afiliacion__id=vendedor_id)
    proveedores = [afiliacion.proveedor_afiliacion for afiliacion in afiliaciones]

    import random
    random.shuffle(proveedores)

    servicios = Servicio_prov.objects.filter(user__in=proveedores).order_by(Random())

    return render(request, 'vendedor/dashboard_vend/list_prov.html', {'proveedores': proveedores, 'profile': profile, 'servicios': servicios })



@login_required(login_url='login_vnd')
def proyecto_pendiente_solic(request):
    user = request.user
    profile = Profile_vendedor.objects.get(user=user)

    solic_proyect = CrearProyecto.objects.filter(vendedor=profile,  estado='Pendiente').order_by('fecha_solicitud')

    context = {
        'profile': profile,
        'solic_proyect': solic_proyect
    }

    return render(request, 'vendedor/dashboard_vend/solicitud_proyec.html', context)





@login_required(login_url='login_vnd')
def details_proyect(request, codigo_unico):


    detail_proyect = CrearProyecto.objects.filter(codigo_unico_proyect=codigo_unico)[0]

    context = {
        'proyecto': detail_proyect
    }

    return render(request, 'vendedor/dashboard_vend/detail_proyect.html', context)



 

@login_required(login_url='login_vnd')
def edit_proyect_vend(request, codigo_unico):
    show_message_alert = False

    user = request.user
    profile = Profile_vendedor.objects.get(user=user)


    edit_proyect = CrearProyecto.objects.get_or_create(vendedor=profile,  codigo_unico_proyect=codigo_unico)[0]


    if request.method == 'POST':
        nombre_de_proyecto = request.POST.get('nombre_proyecto')
        descripcion_de_proyecto = request.POST.get('descripcion_proyecto')
        provincia_de_proyec = request.POST.get('provincias')
        ciudad_de_proyec = request.POST.get('ciudad')
        sector_de_proyec = request.POST.get('sector')
        calle_de_proyec = request.POST.get('calle')
        numero_geo_proyec = request.POST.get('numero')
        apartamen_suite_proyec = request.POST.get('apartamento_suite')
        nombre_client = request.POST.get('nombre_client')
        whatsapp_client = request.POST.get('num_what_client')


        
        if not nombre_de_proyecto: 
            nombre_de_proyecto  = edit_proyect.nombre_proyecto 
        if not descripcion_de_proyecto:
            descripcion_de_proyecto = edit_proyect.descripcion_proyecto
        if not provincia_de_proyec:
            provincia_de_proyec = edit_proyect.provincia_proyec
        if not ciudad_de_proyec:
            ciudad_de_proyec = edit_proyect.ciudad_proyec  
        if not sector_de_proyec:
            sector_de_proyec = edit_proyect.sector_proyec 
        if not calle_de_proyec:
            calle_de_proyec = edit_proyect.calle_proyec
        if not numero_geo_proyec:
            numero_geo_proyec = edit_proyect.numero_proyec
        if not apartamen_suite_proyec:
            apartamen_suite_proyec = edit_proyect.apartamen_suite_proyec
        if not nombre_client:
            nombre_client = edit_proyect.nombre_cliente
        if not whatsapp_client:
            whatsapp_client = edit_proyect.whatsapp

        

        if nombre_de_proyecto.strip() != edit_proyect.nombre_proyecto  or descripcion_de_proyecto.strip() != edit_proyect.descripcion_proyecto or provincia_de_proyec.strip() != edit_proyect.provincia_proyec or ciudad_de_proyec.strip() != edit_proyect.ciudad_proyec or sector_de_proyec.strip() != edit_proyect.sector_proyec or calle_de_proyec.strip() != edit_proyect.calle_proyec or numero_geo_proyec.strip() != edit_proyect.numero_proyec or apartamen_suite_proyec.strip() != edit_proyect.apartamen_suite_proyec or nombre_client.strip() != edit_proyect.nombre_cliente or whatsapp_client.strip() != edit_proyect.whatsapp:

            
            edit_proyect.nombre_proyecto = nombre_de_proyecto.strip()
            edit_proyect.descripcion_proyecto = descripcion_de_proyecto.strip()
            edit_proyect.provincia_proyec = provincia_de_proyec.strip()
            edit_proyect.ciudad_proyec = ciudad_de_proyec.strip()
            edit_proyect.sector_proyec = sector_de_proyec.strip()
            edit_proyect.calle_proyec = calle_de_proyec.strip()
            edit_proyect.numero_proyec = numero_geo_proyec.strip()
            edit_proyect.apartamen_suite_proyec = apartamen_suite_proyec.strip()
            edit_proyect.nombre_cliente = nombre_client.strip()
            edit_proyect.whatsapp = whatsapp_client.strip()
            edit_proyect.save()
            show_message_alert = True



    context = {
        'dataedit': edit_proyect,
         'show_message_alert': show_message_alert,
    }

    return render(request, 'vendedor/dashboard_vend/editar_proyec_vend.html', context)



@login_required(login_url='login_vnd')
def eliminar_proyecto(request, id):
    proyecto = CrearProyecto.objects.get(id=id)
    proyecto.delete()
    
    return redirect('proyecto_pendiente_solic')




########################## ESTADO DEL PROYECTO #################################

@login_required(login_url='login_vnd')
def proyecto_cotizacion(request):
    user = request.user
    profile = Profile_vendedor.objects.get(user=user)

    proyect_cotizacion = CrearProyecto.objects.filter(vendedor=profile,  estado='Cotizacion').order_by('-fecha_solicitud')

    context = {
        'profile': profile,
        'proyect_cotizacion': proyect_cotizacion

    }

    return render(request, 'vendedor/dashboard_vend/cotizacion.html', context)




@login_required(login_url='login_vnd')
def proyecto_activo(request):

    user = request.user
    profile = Profile_vendedor.objects.get(user=user)

    proyect_activo = CrearProyecto.objects.filter(vendedor=profile,  estado='Activado').order_by('fecha_aprobacion')

    context = {
        'profile': profile,
        'proyect_activo': proyect_activo,
    }

    return render(request, 'vendedor/dashboard_vend/proyectos_activos.html', context)




@login_required(login_url='login_vnd')
def proyecto_concluido(request):
    
    user = request.user
    profile = Profile_vendedor.objects.get(user=user)

    proyect_concluido = CrearProyecto.objects.filter(vendedor=profile,  estado='Concluido').order_by('-fecha_solicitud')

    context = {
        'profile': profile,
        'proyect_concluido': proyect_concluido
    }

    return render(request, 'vendedor/dashboard_vend/proyect_concluido.html', context)




@login_required(login_url='login_vnd')
def proyecto_suspendido(request):
    
    user = request.user
    profile = Profile_vendedor.objects.get(user=user)

    proyect_suspendido = CrearProyecto.objects.filter(vendedor=profile,  estado='Suspendido').order_by('-fecha_solicitud')

    context = {
        'profile': profile,
        'proyect_suspendido': proyect_suspendido
    }

    return render(request, 'vendedor/dashboard_vend/proyecto_suspendido.html', context)





@login_required(login_url='login_vnd')
def proyecto_delete(request):
    
    user = request.user
    profile = Profile_vendedor.objects.get(user=user)

    proyect_delete = CrearProyecto.objects.filter(vendedor=profile,  estado='Cancelado').order_by('-fecha_solicitud')

    context = {
        'profile': profile,
        'proyect_delete': proyect_delete
    }

    return render(request, 'vendedor/dashboard_vend/proyect_delet.html', context)



################################### ESTADO LA LAS COMISIONES ############################



@login_required(login_url='login_vnd')
def proyecto_comision_pendiente(request):
    
    user = request.user
    profile = Profile_vendedor.objects.get(user=user)

    comision_pendiente = CrearProyecto.objects.filter(vendedor=profile,  estado_de_comision_vend='Pendiente')

    context = {
        'profile': profile,
        'comision_pendient': comision_pendiente
    }

    return render(request, 'vendedor/dashboard_vend/comision_pendiente.html', context)







################################## FACTURA COMISIONES #####################################

@login_required(login_url='login_vnd')
def factura_comision_vend(request):

    now = timezone.now()

    ten_minutes_ago = now - timezone.timedelta(days=7)

    user = request.user
    profile = Profile_vendedor.objects.get(user=user)

    factura_comision = Comisiones_vendedor.objects.filter(vendedor_comi_fk = profile, fecha_facturacion__gte=ten_minutes_ago)

    context = {
        'factura_comision': factura_comision
    }

    return render(request, 'vendedor/dashboard_vend/deposito_reciente.html', context)




@login_required(login_url='login_vnd')
def detail_factura_vendedor(request, codigo_factura):

    user = request.user
    profile = Profile_vendedor.objects.get(user=user)

    factura_comision = Comisiones_vendedor.objects.filter(
        vendedor_comi_fk=profile,  codigo_factura_comision_ved=codigo_factura
    )

    context = {
        'factura_comision': factura_comision
    }

    return render(request, 'vendedor/dashboard_vend/factua_comision_vend.html', context)




@login_required(login_url='login_vnd')
def historial_de_pagos(request):
    now = datetime.now()
    seven_days_ago = now - timedelta(days=7)
    user = request.user
    profile = Profile_vendedor.objects.get(user=user)

    histori_factura_comision = Comisiones_vendedor.objects.filter(
        vendedor_comi_fk=profile, fecha_facturacion__lte=seven_days_ago
    )

    context = {
        'histori_factura_comision': histori_factura_comision
    }

    return render(request, 'vendedor/dashboard_vend/historial_deposito.html', context)



@login_required(login_url='login_vnd')
def proyecto_historial(request):
    
    user = request.user
    profile = Profile_vendedor.objects.get(user=user)

    proyect_histori = CrearProyecto.objects.filter(vendedor=profile, estado__in=['Concluido', 'Cancelado', 'Suspendido'])

    context = {
        'profile': profile,
        'proyect_histori': proyect_histori
    }

    return render(request, 'vendedor/dashboard_vend/proyect_histori.html', context)





########################### DUDAS Y COMENTARIOS ######################################

@login_required(login_url='login_vnd')
def create_message_duda_comentario(request):

    show_message_alert = False

    user = request.user

    if request.method == 'POST':
        nombre_asunto = request.POST.get('asunto')
        mensage_du_co = request.POST.get('mensaje')

        vendedorfk = get_object_or_404(Profile_vendedor, user=user)

        contact_vendfk = get_object_or_404(Contacto_vendedor, user=vendedorfk.id)

        crea_mensage = Duda_comentario.objects.create(
            asunto_mensaage = nombre_asunto,
            texto_mensage = mensage_du_co,
            vendedor_fk = vendedorfk,
            contact_vend_fk = contact_vendfk,
        )
        
        crea_mensage.save()
        show_message_alert = True

    context = {
        'show_message_alert': show_message_alert,
    }

    return render(request, 'vendedor/mensage/duda_comentario.html', context)