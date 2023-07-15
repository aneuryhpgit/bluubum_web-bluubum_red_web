from django.shortcuts import render
from django.shortcuts import get_object_or_404, render, redirect
from django.http import Http404
from django.contrib.auth.decorators import login_required
from perfil_proveedor.models import Profile_proveedor, Confirmacion
from login_vendedor.models import Profile_vendedor
from prov_servis.models import Servicio_prov
from config_inicial_prov.models import Ubicacion_proveedor, Rango_servicio
from dashboard_prov.models import Afiliacion, CrearProyecto

# Create your views here.




@login_required
def afiliacion_view(request):
    if request.method == 'POST':
        proveedor_id = request.POST.get('proveedor_id')
        proveedor = Profile_proveedor.objects.get(id=proveedor_id)
        vendedor = request.user.profile_vendedor
        afiliacion = Afiliacion(
            proveedor_afiliacion=proveedor,
            vendedor_afiliacion=vendedor,
            estado='Pendiente'
        )
        afiliacion.save()
        return redirect('vista_perfil_proveedor', codigo_unico=proveedor.codigo_unico_proveedor)








@login_required
def vista_perfil_proveedor(request, codigo_unico):

    proveedor = get_object_or_404(Profile_proveedor, codigo_unico_proveedor=codigo_unico)
    servicios = Servicio_prov.objects.filter(user=proveedor).order_by('-timestamp')
    ubicacion = Ubicacion_proveedor.objects.filter(user=proveedor)
    geoservi = Rango_servicio.objects.filter(user=proveedor)
    
    # Verificar si el usuario conectado es un vendedor
    if request.user.is_authenticated and hasattr(request.user, 'profile_vendedor'):
        vendedor = request.user.profile_vendedor
        afiliacion = Afiliacion.objects.filter(proveedor_afiliacion=proveedor, vendedor_afiliacion=vendedor).first()
        esta_afiliado = afiliacion is not None
    else:
        vendedor = None
        afiliacion = None
        esta_afiliado = False

    
    context = {
        'proveedor': proveedor,
        'servicios': servicios,
        'ubicacion': ubicacion,
        'geoservi': geoservi,

        'afiliacion': afiliacion,
        'esta_afiliado': esta_afiliado,
    }

    return render(request, 'proveedor/perfil_proveedor.html', context)





@login_required(login_url='login_vnd')
def vista_perfil_vendedor(request, codigo_unico_vend):

    user = request.user
    profile = Profile_vendedor.objects.get(user=user)
    vendedor = get_object_or_404(Profile_vendedor, codigo_unico_vendedor=codigo_unico_vend)


    try:
        confirmacion = Confirmacion.objects.get(user=user)
        if not confirmacion.confirmado:
            return redirect('confirmar_usuario_vend')
    except Confirmacion.DoesNotExist:
        return redirect('confirmar_usuario_vend')

    proyecto_solicitud_num = CrearProyecto.objects.filter(vendedor=profile, estado='Pendiente').count()

    proyecto_cotizacion_num = CrearProyecto.objects.filter(vendedor=profile, estado='Cotizacion').count()

    proyecto_activo_num = CrearProyecto.objects.filter(vendedor=profile, estado='Activado').count()

    proyecto_concluido_num = CrearProyecto.objects.filter(vendedor=profile, estado='Concluido').count()

    proyecto_comision_num = CrearProyecto.objects.filter(vendedor=profile, estado_de_comision_vend='Pendiente').count()

    proyec_comision_saldado_num = CrearProyecto.objects.filter(vendedor=profile, estado_de_comision_vend='Pagado').count()

    proyecto_suspend_num = CrearProyecto.objects.filter(vendedor=profile, estado='Suspendido').count()

    proyecto_cancelado_num = CrearProyecto.objects.filter(vendedor=profile, estado='Cancelado').count()

    context = {
        'vendedor': vendedor,
        'proyecto_solicitud_num': proyecto_solicitud_num,
        'proyecto_cotizacion_num': proyecto_cotizacion_num,
        'proyecto_activo_num': proyecto_activo_num,
        'proyecto_concluido_num': proyecto_concluido_num,
        'proyecto_comision_num': proyecto_comision_num,
        'proyec_comision_saldado_num': proyec_comision_saldado_num,
        'proyecto_suspend_num': proyecto_suspend_num,
        'proyecto_cancelado_num': proyecto_cancelado_num,
    }

    return render(request, 'vendedor/dashboard_vend/perfil_vendedor.html', context)








