from django.shortcuts import render
from django.shortcuts import get_object_or_404, render, redirect

from perfil_proveedor.models import Profile_proveedor
from .models import Afiliacion, CrearProyecto, Comisiones_vendedor
from login_vendedor.models import Profile_vendedor
from vend_config_inic.models import Contacto_vendedor, Direccion_vendedor, Metodo_pago_vendedor
from dashboard_prov.models import Afiliacion
from prov_servis.models import Servicio_prov
from decimal import Decimal
from datetime import date
from django.utils import timezone

from django.http import Http404
from django.contrib.auth.decorators import login_required



from django.http import HttpResponseForbidden
# Create your views here.


@login_required(login_url='login_proveedor')
def dashboard_prov(request):



    user = request.user
    profile = Profile_proveedor.objects.get(user=user)

    proyecto_solicitud_num= CrearProyecto.objects.filter(proveedor=profile, estado='Pendiente').count()

    proyecto_cotiz_num= CrearProyecto.objects.filter(proveedor=profile, estado='Cotizacion').count()

    proyecto_activo_num= CrearProyecto.objects.filter(proveedor=profile, estado='Activado').count()

    proyecto_concluido_num= CrearProyecto.objects.filter(proveedor=profile, estado='Concluido').count()

    proyecto_suspendido_num= CrearProyecto.objects.filter(proveedor=profile, estado='Suspendido').count()

    proyecto_cancelado_num= CrearProyecto.objects.filter(proveedor=profile, estado='Cancelado').count()

    proyecto_comis_pendient_num= CrearProyecto.objects.filter(proveedor=profile, estado_comis_plataform='Pendiente').count()

    proyecto_comis_pendient_vend_num= CrearProyecto.objects.filter(proveedor=profile, estado_comis_plataform='Saldado', estado_de_comision_vend='Pendiente', ).count()

    proyecto_comis_saldada_num= CrearProyecto.objects.filter(proveedor=profile, estado_comis_plataform='Saldado').count()

    proyecto_comis_pagado_vend_num= CrearProyecto.objects.filter(proveedor=profile, estado_de_comision_vend='Pagado', ).count()

    afiliado_vendedores_num = Afiliacion.objects.filter(proveedor_afiliacion=profile).count()

    context = {
        'profile': profile,
        'proyecto_solicitud_num': proyecto_solicitud_num,
        'proyecto_cotiz_num': proyecto_cotiz_num,
        'proyecto_activo_num': proyecto_activo_num,
        'proyecto_concluido_num': proyecto_concluido_num,
        'proyecto_suspendido_num': proyecto_suspendido_num,
        'proyecto_cancelado_num': proyecto_cancelado_num,
        'proyecto_comis_pendient_num': proyecto_comis_pendient_num,
        'proyecto_comis_pendient_vend_num': proyecto_comis_pendient_vend_num,
        'proyecto_comis_saldada_num': proyecto_comis_saldada_num,
        'proyecto_comis_pagado_vend_num': proyecto_comis_pagado_vend_num,
        'afiliado_vendedores_num': afiliado_vendedores_num,
    }

    return render(request, 'proveedor/dahsboard/tablero_prov.html', context)




###################################################################################
################## CREAR PROYECTO FUNCION VENDEDOR ################################
###################################################################################
@login_required(login_url='login_vnd')
def Crear_nuevo_proyecto(request, codigo_unico):

    show_message_alert = False
    
    proveedor = get_object_or_404(Profile_proveedor, codigo_unico_proveedor=codigo_unico)
    vendedor_user = request.user.profile_vendedor
    profile = get_object_or_404(Profile_vendedor, user=vendedor_user.user)

    # Verificar si el vendedor está afiliado al proveedor de la vista actual
    afiliacion = Afiliacion.objects.filter(vendedor_afiliacion=profile, proveedor_afiliacion=proveedor).first()
    if not afiliacion:
        return HttpResponseForbidden()
    
    servicios = Servicio_prov.objects.filter(user=proveedor)


    if request.method == 'POST':
        nombre_de_proyecto = request.POST.get('nombre_proyecto')
        tipo_de_servicio = request.POST.get('tipo_servicio')
        servicio = get_object_or_404(Servicio_prov, id=tipo_de_servicio)
        descripcion_de_proyecto = request.POST.get('descripcion_proyecto')
        provincia_de_proyec = request.POST.get('provincias')
        ciudad_de_proyec = request.POST.get('ciudad')
        sector_de_proyec = request.POST.get('sector')
        calle_de_proyec = request.POST.get('calle')
        numero_geo_proyec = request.POST.get('numero')
        apartamen_suite_proyec = request.POST.get('apartamento_suite')
        nombre_client = request.POST.get('nombre_client')
        whatsapp_client = request.POST.get('num_what_client')


        proveedor_foreink = Profile_proveedor.objects.filter(user=proveedor.user).first()
        proveedor_foreink.save()

        vendedor_forenk = Profile_vendedor.objects.filter(user=profile.user).first()
        vendedor_forenk.save()

        afiliacion_vend = Afiliacion.objects.filter(vendedor_afiliacion=profile.id).first()
        afiliacion_vend.save()

        contacto_vendedor = Contacto_vendedor.objects.filter(user=profile).first()
        contacto_vendedor.save()

        crear_proyecto = CrearProyecto(

            nombre_proyecto = nombre_de_proyecto,
            servicio = servicio,
            descripcion_proyecto = descripcion_de_proyecto,
            provincia_proyec = provincia_de_proyec,
            ciudad_proyec = ciudad_de_proyec,
            sector_proyec = sector_de_proyec,
            calle_proyec = calle_de_proyec, 
            numero_proyec = numero_geo_proyec,
            apartamen_suite_proyec = apartamen_suite_proyec,
            nombre_cliente = nombre_client,
            whatsapp = whatsapp_client,

            proveedor = proveedor_foreink,
            vendedor = vendedor_forenk,
            afiliacion = afiliacion_vend,
            contact_vendedor = contacto_vendedor
            
        ) 
        crear_proyecto.save()
        show_message_alert = True


    context = {
        'servicios': servicios, 
        'proveedor': proveedor,
        'show_message_alert': show_message_alert,
    }

    return render(request, 'vendedor/dashboard_vend/crear_proyecto.html', context)



############################################################################################
############################################################################################



################################## SOLICITUD DE PROYECTO #################################
@login_required(login_url='login_proveedor')
def solicitu_proyecto_prov(request):

    user = request.user
    profile = Profile_proveedor.objects.get(user=user)

    proyecto_solicitud = CrearProyecto.objects.filter(proveedor=profile,  estado='Pendiente')

    
    context = {
        'proyecto_solicitud': proyecto_solicitud,
    }

    return render(request, 'proveedor/dahsboard/solicitud_proyecto.html', context)




@login_required(login_url='login_proveedor')
def solicitu_enviar_acotizacion(request, codigo_unico):

    show_message_alert = False
    
    user = request.user
    profile = Profile_proveedor.objects.get(user=user)

    envi_cotiz = CrearProyecto.objects.get_or_create(proveedor=profile,  codigo_unico_proyect=codigo_unico)[0]

    if request.method == 'POST':
        fecha_cotiz = request.POST.get('fecha_cotizacion')
        cotizacion_data = request.POST.get('cotizacion')

        envi_cotiz.fecha_disponible_cotizacion = fecha_cotiz
        envi_cotiz.estado = cotizacion_data
        envi_cotiz.save()
        show_message_alert = True
    
    context = {
        'envi_cotiz': envi_cotiz,
        'show_message_alert': show_message_alert,
        
    }

    return render(request, 'proveedor/dahsboard/enviar_a_cotizacion.html', context)





@login_required(login_url='login_proveedor')
def delete_solicitud_proyect_prov(request, id):
    solict_delete = CrearProyecto.objects.get(id=id)
    solict_delete.delete()
    return redirect('solicitu_proyecto_prov')




############################## COTIZACION  ###########################

@login_required(login_url='login_proveedor')
def proyecto_cotizacion_prov(request):

    user = request.user
    profile = Profile_proveedor.objects.get(user=user)

    proyecto_cotizacion= CrearProyecto.objects.filter(proveedor=profile,  estado='Cotizacion').order_by('fecha_aprobacion')

    
    context = {
        'proyecto_cotizacion': proyecto_cotizacion
    }

    return render(request, 'proveedor/dahsboard/cotizacion_list_proyect.html', context)




@login_required(login_url='login_proveedor')
def aprovar_acotizacion(request, codigo_unico):
    
    show_message_alert = False
    
    user = request.user
    profile = Profile_proveedor.objects.get(user=user)

    cotizar = CrearProyecto.objects.get_or_create(proveedor=profile,  codigo_unico_proyect=codigo_unico)[0]

    if request.method == 'POST':
        fecha_aprobacion = request.POST.get('fecha_aprobacionn')
        estado_proyect = request.POST.get('activar_proyect')
        fecha_nicio = request.POST.get('fecha_inicio')
        fecha_comis_pago = request.POST.get('fecha_pago_comision')
        fecha_comis_pago_vend = request.POST.get('fecha_pago_comision_vend')
        fecha_estimada_conclucion = request.POST.get('fecha_estimada_conclucion')
        precio_proyect = Decimal(request.POST.get('precio_proyect'))
        nom_client = request.POST.get("nombre_cliente")
        tel_client = request.POST.get("tel_client")
        descriccion_proyec = request.POST.get("decriccion_proyect")

        porciento_comis = cotizar.servicio.Comicion

        transform_decimal = porciento_comis / Decimal('100.0')
        total_comis = transform_decimal*precio_proyect

        comision_vendedor = total_comis* Decimal('0.7')
        comision_prov = total_comis* Decimal('0.3')



        # Asigna los valores existentes del modelo si no se proporcionan nuevos datos
        if not nom_client:
            nom_client = cotizar.nombre_cliente
        if not tel_client:
            tel_client = cotizar.telefono
        if not descriccion_proyec:
            descriccion_proyec = cotizar.descripcion_proyecto

        if fecha_aprobacion != cotizar.fecha_aprobacion or estado_proyect != cotizar.estado or fecha_nicio != cotizar.fecha_estimada_inicio or fecha_estimada_conclucion != cotizar.fecha_estimada_conclusion or precio_proyect != cotizar.precio or comision_vendedor != cotizar.comision_vendedor or comision_prov != cotizar.comision_prov or nom_client != cotizar.nombre_cliente or tel_client != cotizar.telefono or descriccion_proyec != cotizar.descripcion_proyecto:

            cotizar.fecha_aprobacion = fecha_aprobacion
            cotizar.estado = estado_proyect 
            cotizar.fecha_estimada_inicio = fecha_nicio

            cotizar.fecha_pago_comision = fecha_comis_pago
            cotizar.fecha_pago_comision_vend = fecha_comis_pago_vend
            cotizar.fecha_estimada_conclusion = fecha_estimada_conclucion
            cotizar.precio = precio_proyect
            cotizar.comision_plataform = total_comis
            cotizar.comision_vendedor = comision_vendedor
            cotizar.comision_prov = comision_prov

            cotizar.nombre_cliente = nom_client
            cotizar.telefono = tel_client
            cotizar.descripcion_proyecto = descriccion_proyec

            cotizar.estado_de_comision_vend = "Pendiente"
            cotizar.estado_comis_plataform = "Pendiente"
            cotizar.save()

            show_message_alert = True
    
    context = {
        'cotizar': cotizar,
        'show_message_alert': show_message_alert, 
    }

    return render(request, 'proveedor/dahsboard/aprovar_cotizacion.html', context)





########################## lista proyectos activados #################################
@login_required(login_url='login_proveedor')
def proyecto_activado_prov(request):
    
    user = request.user
    profile = Profile_proveedor.objects.get(user=user)

    proyecto_activo= CrearProyecto.objects.filter(proveedor=profile,  estado='Activado').order_by('fecha_aprobacion')

    
    context = {
        'proyecto_activo': proyecto_activo
    }

    return render(request, 'proveedor/dahsboard/proyecto_activado.html', context)





#############################  concluir proyecto activo #########################
@login_required(login_url='login_proveedor')
def concluir_proyecto_activo(request, codigo_unico):
    
    show_message_alert = False
    
    user = request.user
    profile = Profile_proveedor.objects.get(user=user)

    envi_concluir = CrearProyecto.objects.get_or_create(proveedor=profile,  codigo_unico_proyect=codigo_unico)[0]

    if request.method == 'POST':
        estado_proyect = request.POST.get('proyect_concluido')

        envi_concluir.fecha_conclusion = timezone.now()
        envi_concluir.estado = estado_proyect
        envi_concluir.save()
        show_message_alert = True
    
    context = {
        'envi_concluir': envi_concluir,
        'show_message_alert': show_message_alert,
        
    }

    return render(request, 'proveedor/dahsboard/concluir_proyect.html', context)




########################## lista de proyectos concluidos ######################

@login_required(login_url='login_proveedor')
def proyecto_concluido_prov(request):
    
    user = request.user
    profile = Profile_proveedor.objects.get(user=user)

    proyecto_concluido = CrearProyecto.objects.filter(proveedor=profile,  estado='Concluido')

    
    context = {
        'proyecto_concluido': proyecto_concluido
    }

    return render(request, 'proveedor/dahsboard/proyect_concluido.html', context)




########################## suspender proyecto #############################################
@login_required(login_url='login_proveedor')
def suspender_proyecto_activo(request, codigo_unico):
    
    show_message_alert = False
    
    user = request.user
    profile = Profile_proveedor.objects.get(user=user)

    envi_suspender = CrearProyecto.objects.get_or_create(proveedor=profile,  codigo_unico_proyect=codigo_unico)[0]

    if request.method == 'POST':
        estado_proyect = request.POST.get('proyect_suspendido')

        envi_suspender.fecha_suspencion_proyec = timezone.now()
        envi_suspender.estado = estado_proyect
        envi_suspender.save()
        show_message_alert = True
    
    context = {

        'envi_suspender': envi_suspender,
        'show_message_alert': show_message_alert,
        
    }

    return render(request, 'proveedor/dahsboard/suspender_proyect.html', context)



@login_required(login_url='login_proveedor')
def proyecto_suspendido_prov(request):
    
    user = request.user
    profile = Profile_proveedor.objects.get(user=user)

    proyecto_suspendido = CrearProyecto.objects.filter(proveedor=profile,  estado='Suspendido')

    
    context = {
        'proyecto_suspendido': proyecto_suspendido
    }

    return render(request, 'proveedor/dahsboard/proyect_suspendido_list.html', context)



@login_required(login_url='login_proveedor')
def reactivar_proyecto_suspendido(request, codigo_unico):
    
    show_message_alert = False
    
    user = request.user
    profile = Profile_proveedor.objects.get(user=user)

    envi_react = CrearProyecto.objects.get_or_create(proveedor=profile,  codigo_unico_proyect=codigo_unico)[0]

    if request.method == 'POST':
        estado_proyect = request.POST.get('activar')

        envi_react.fecha_reanudacion_proyec = timezone.now()
        envi_react.estado = estado_proyect
        envi_react.save()
        show_message_alert = True
    
    context = {

        'envi_react': envi_react,
        'show_message_alert': show_message_alert,
        
    }

    return render(request, 'proveedor/dahsboard/reanudar_proyect_suspendido.html', context)



@login_required(login_url='login_proveedor')
def cancelar_proyecto_suspendido(request, codigo_unico):
    
    show_message_alert = False
    
    user = request.user
    profile = Profile_proveedor.objects.get(user=user)

    envi_cancelar = CrearProyecto.objects.get_or_create(proveedor=profile,  codigo_unico_proyect=codigo_unico)[0]

    if request.method == 'POST':
        estado_proyect = request.POST.get('proyect_cancelar')

        envi_cancelar.fecha_cancelacion_proyec = timezone.now()
        envi_cancelar.estado = estado_proyect
        envi_cancelar.save()
        show_message_alert = True
    
    context = {

        'envi_cancelar': envi_cancelar,
        'show_message_alert': show_message_alert,
        
    }

    return render(request, 'proveedor/dahsboard/cancelar_proyecto_suspendido.html', context)




############################### Cancelar proyecto ##################################
@login_required(login_url='login_proveedor')
def cancelar_proyecto_activo(request, codigo_unico):
    
    show_message_alert = False
    
    user = request.user
    profile = Profile_proveedor.objects.get(user=user)

    envi_cancelar = CrearProyecto.objects.get_or_create(proveedor=profile,  codigo_unico_proyect=codigo_unico)[0]

    if request.method == 'POST':
        estado_proyect = request.POST.get('proyect_cancelar')

        envi_cancelar.fecha_cancelacion_proyec = timezone.now()
        envi_cancelar.estado = estado_proyect
        envi_cancelar.save()
        show_message_alert = True
    
    context = {

        'envi_cancelar': envi_cancelar,
        'show_message_alert': show_message_alert,
        
    }

    return render(request, 'proveedor/dahsboard/cancelar_proyect.html', context)


@login_required(login_url='login_proveedor')
def proyecto_cancelado_prov(request):
    
    user = request.user
    profile = Profile_proveedor.objects.get(user=user)

    proyecto_cancelado = CrearProyecto.objects.filter(proveedor=profile,  estado='Cancelado')

    
    context = {
        'proyecto_cancelado': proyecto_cancelado
    }

    return render(request, 'proveedor/dahsboard/cancelado_list_proyect.html', context)



############################## Proyecto #################################
@login_required(login_url='login_proveedor')
def proyecto_detail_prov(request, codigo_unico):
    
    user = request.user
    profile = Profile_proveedor.objects.get(user=user)

    proyecto_detail = CrearProyecto.objects.filter(proveedor=profile, codigo_unico_proyect=codigo_unico)[0]

    
    context = {
        'proyecto_detail': proyecto_detail
    }

    return render(request, 'proveedor/dahsboard/details_proyect.html', context)




######################### Comisiones ###############################
@login_required(login_url='login_proveedor')
def proyecto_comision(request):

    fecha_actual = date.today()
    
    user = request.user
    profile = Profile_proveedor.objects.get(user=user)

    proyecto_comision_pend = CrearProyecto.objects.filter(proveedor=profile,   estado_comis_plataform ='Pendiente')

    
    context = {
        'proyecto_comision_pend': proyecto_comision_pend,
        'fecha_actual': fecha_actual,
    }

    return render(request, 'proveedor/dahsboard/comision/comis_pendient_plataform.html', context)




####################### Saldar comision #################
@login_required(login_url='login_proveedor')
def saldar_comision(request, codigo_unico):

   
    
    show_message_alert = False
    
    user = request.user
    profile = Profile_proveedor.objects.get(user=user)

    pago_comis = CrearProyecto.objects.get_or_create(proveedor=profile,  codigo_unico_proyect=codigo_unico)[0]

    if request.method == 'POST':
        estado_proyect = request.POST.get('saldar_comis')

        pago_comis.fecha_saldado_comis = timezone.now()
        pago_comis.estado_comis_plataform = estado_proyect

        pago_comis.save()

        show_message_alert = True
    
    context = {

        'pago_comis': pago_comis,
        'show_message_alert': show_message_alert,
        
    }

    return render(request, 'proveedor/dahsboard/comision/saldar_comision.html', context)





############################ SALDAR COMISION VENDEDOR #################################
@login_required(login_url='login_proveedor')
def list_comision_pendiente_vend(request):
    
    fecha_actual = date.today()
    
    user = request.user
    profile = Profile_proveedor.objects.get(user=user)

    comision_vend = CrearProyecto.objects.filter(proveedor=profile,   estado_comis_plataform ='Saldado', estado_de_comision_vend = 'Pendiente' )

    
    context = {
        'comision_vend': comision_vend,
        'fecha_actual': fecha_actual,
    }

    return render(request, 'proveedor/dahsboard/comision/vend_comis_pendiente.html', context)




@login_required(login_url='login_proveedor')
def saldar_comision_vendedor(request, codigo_unico):
        
        show_message_alert = False


        user = request.user
        profile = get_object_or_404(Profile_proveedor, user=user)

        pago_comis_vendedor, created = CrearProyecto.objects.get_or_create(proveedor=profile, codigo_unico_proyect=codigo_unico)


        vendedor_username = pago_comis_vendedor.vendedor.user  # Obtiene el nombre de usuario del vendedor como cadena de texto
        vendedor = Profile_vendedor.objects.get(user=vendedor_username)
        
 
        direccion_vend = Direccion_vendedor.objects.filter(user=vendedor)
        mtdvend = Metodo_pago_vendedor.objects.filter(user=vendedor)


        if direccion_vend is None:
            raise Http404("No se encontró una dirección de vendedor para este usuario.")


        if request.method == 'POST':
            intitucion_deposito = request.POST.get('name_institucion')

            proyecto_comision = get_object_or_404(CrearProyecto, id=pago_comis_vendedor.id)
            proyecto_comision.save()

            proveedor_comision_fk = get_object_or_404(Profile_proveedor, user=pago_comis_vendedor.proveedor.user)
            vendedor_comision_fk = get_object_or_404(Profile_vendedor, user=pago_comis_vendedor.vendedor.user)
            direcc_comis_vend_fk = get_object_or_404(Direccion_vendedor, user=vendedor)
            metd_comis_vend = get_object_or_404(Metodo_pago_vendedor, user=vendedor)

            crea_factura = Comisiones_vendedor.objects.create(
                proyecto_comi=proyecto_comision,
                proveedor_comi_fk=proveedor_comision_fk,
                vendedor_comi_fk=vendedor_comision_fk,
                direccion_comi_fk=direcc_comis_vend_fk,
                metd_pg_vend_comi_fk=metd_comis_vend,
                institucion_deposito = intitucion_deposito
            )

            pago_comis_vendedor.estado_de_comision_vend = 'Pagado'

            crea_factura.save()
            pago_comis_vendedor.save()

            show_message_alert = True
        
    
        context = {
            'pcv': pago_comis_vendedor,
            'direccion_vend': direccion_vend,
            'mtdvend': mtdvend,
            'show_message_alert': show_message_alert,
        }

        return render(request, 'proveedor/dahsboard/comision/vend_saldar_comision.html', context)




################################# HISTORIAL COMISIONES  ########################################
@login_required(login_url='login_proveedor')
def history_comision(request):
    
    fecha_actual = date.today()
    
    user = request.user
    profile = Profile_proveedor.objects.get(user=user)

    comision_platafroma = CrearProyecto.objects.filter(proveedor=profile,   estado_comis_plataform ='Saldado')

    
    context = {
        'comision_plat': comision_platafroma,
        'fecha_actual': fecha_actual,
    }

    return render(request, 'proveedor/dahsboard/comision/historial_comisiones.html', context)





@login_required(login_url='login_proveedor')
def history_comision_vendedores(request):
    
    user = request.user
    profile = Profile_proveedor.objects.get(user=user)

    comision_vendedores = CrearProyecto.objects.filter(proveedor=profile, estado_de_comision_vend = 'Pagado')

    
    context = {
        'comision_vendedores': comision_vendedores,
       
    }

    return render(request, 'proveedor/dahsboard/comision/historial_comision_vendedores.html', context)





@login_required(login_url='login_proveedor')
def history_afiliados_vendedores(request):
    
    fecha_actual = date.today()
    
    user = request.user
    profile = Profile_proveedor.objects.get(user=user)

    afiliado_vendedores = Afiliacion.objects.filter(proveedor_afiliacion=profile)

    
    context = {
        'afiliado_vendedores': afiliado_vendedores,
        'fecha_actual': fecha_actual,
    }

    return render(request, 'proveedor/dahsboard/comision/historial_de_afiliados_vendedores.html', context)










