from django.views.generic import TemplateView
from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import render, redirect, get_object_or_404
from perfil_proveedor.models import Profile_proveedor
from config_inicial_prov.models import Contacto_proveedor, Ubicacion_proveedor, Rango_servicio
from .models import Servicio_prov, Post_prov
import uuid
from django.utils.text import slugify
from storages.backends.gcloud import GoogleCloudStorage
from django.conf import settings
from django.core.files.storage import default_storage



# Create your views here.



@login_required(login_url='home_page')
def crear_servicio(request):
    user = request.user
    profile = get_object_or_404(Profile_proveedor, user=user)
    servicioList = profile.servicio.all().order_by('-timestamp')

    if request.method == 'POST':
        nombre_servicio = request.POST.get('nombre_servico')
        imagen_servicio = request.FILES.get('imagen')
        descripcion = request.POST.get('descripcion')
        comision = request.POST.get('comision')
        
        contacto_proveedor = Contacto_proveedor.objects.filter(user=profile).first()
        contacto_proveedor.save()

        ubicacion_proveedor = Ubicacion_proveedor.objects.filter(user=profile).first()
        ubicacion_proveedor.save()

        geo_servicios = Rango_servicio.objects.filter(user=profile).first()
        geo_servicios.save()

        if imagen_servicio != None:
            
            servicio = Servicio_prov(
                nombre_servicio=nombre_servicio,
                descripcion_serv = descripcion,
                Comicion=float(comision),
                user=profile,
                contactoProveedor_forenkey=contacto_proveedor,
                ubicacionProveedor_forenkey=ubicacion_proveedor,
                geoServiciosProveedor_forenkey=geo_servicios
            )

            # Guardar las imágenes en el almacenamiento en la nube
            image_path_servicio = f'{settings.PUBLIC_MEDIA_LOCATION}/{imagen_servicio.name}'
            storage = GoogleCloudStorage()
            storage.save(image_path_servicio, imagen_servicio)
            servicio.imagen_servicio = image_path_servicio

            servicio.save()

            return redirect('crea_servicio_prov')
    
    context = {
        'servicioList': servicioList,
        'profile': profile,
    }

  
    return render(request, 'proveedor/servicio_proveedor/serviciosprov.html', context)



#-----------------------EDITAR SERVICIO-----------------------------
@login_required
def editar_servicio_prov(request, id):
    editar_ser = get_object_or_404(Servicio_prov, id=id)

    if request.method == 'POST':
        nombre_servicio_edit = request.POST.get('nombre_servico')
        imagen_servicio_edit = request.FILES.get('imagen')
        descripcion = request.POST.get('descripcion')
        comision_edit = request.POST.get('comision')

        # Asigna los valores existentes del modelo si no se proporcionan nuevos datos
        if not nombre_servicio_edit:
            nombre_servicio_edit = editar_ser.nombre_servicio
        if not imagen_servicio_edit:
            imagen_servicio_edit = editar_ser.imagen_servicio
        if not descripcion:
            descripcion = editar_ser.descripcion_serv
        if not comision_edit:
            comision_edit = editar_ser.Comicion

        # Actualiza los campos del modelo si se proporcionan nuevos datos
        if nombre_servicio_edit.strip() !=  editar_ser.nombre_servicio or imagen_servicio_edit != editar_ser.imagen_servicio or descripcion.strip() != editar_ser.descripcion_serv or comision_edit != editar_ser.Comicion:


            # Guardar las imágenes en el almacenamiento en la nube
            if imagen_servicio_edit:
                image_path_servicio = f'{settings.PUBLIC_MEDIA_LOCATION}/{imagen_servicio_edit.name}'
                storage = GoogleCloudStorage()
                storage.save(image_path_servicio, imagen_servicio_edit)
                editar_ser.imagen_servicio = image_path_servicio

            editar_ser.nombre_servicio = nombre_servicio_edit.strip()
            editar_ser.descripcion_serv = descripcion
            editar_ser.Comicion = comision_edit
            editar_ser.save()

    
    context = {
        'dato_actual': editar_ser
    }

    return render(request, 'proveedor/servicio_proveedor/editar_servicio.html', context)



#-----------------------Eliminar Servicio---------------------

def delete_image_from_storage(image_path):
    storage = GoogleCloudStorage()
    storage.delete(image_path)




##servi_delete = Servicio_prov.objects.get(id=id)


 #   # Obtén la ruta de la imagen del servicio
 #   image_path = servi_delete.imagen_servicio

    # Elimina el servicio
  #  servi_delete.delete()

    # Elimina la imagen del almacenamiento en la nube
  #  delete_image_from_storage(image_path)


  #  return redirect('crea_servicio_prov')


@login_required
def eliminar_servicio_prov(request, id):
    servi_delete = Servicio_prov.objects.get(id=id)

    # Obtén la imagen del servicio
    imagen_servicio = servi_delete.imagen_servicio

    # Elimina el servicio
    servi_delete.delete()

    # Elimina la imagen del almacenamiento en la nube
    if imagen_servicio:
        imagen_servicio.delete()

    return redirect('crea_servicio_prov')



#////////////////////////////// POST /////////////////////////////////////

@login_required
def crear_post_prov(request):
    # Obtener todos los servicios de la base de datos del usuario proveedor
    user = request.user 
    proveedor = get_object_or_404(Profile_proveedor, user=user)
    codigo_unico = proveedor.codigo_unico_proveedor

    proveedor = get_object_or_404(Profile_proveedor, codigo_unico_proveedor=codigo_unico)
    post = Servicio_prov.objects.filter(user=proveedor)
    
    servicios = user.profile_proveedor.servicio.all()
    profile = get_object_or_404(Profile_proveedor, user=user)
    post_list = profile.posts.all().order_by('-fecha_creacion')
    if request.method == 'POST':
        # Obtener los datos del formulario
        titulo = request.POST.get('titulo')
        imagen_serv = request.FILES.get('imagen_serv', None)
        imagen_serv_dos = request.FILES.get('imagen_serv_dos', None)
        imagen_serv_tres = request.FILES.get('imagen_serv_tres', None)
        imagen_serv_cuatro = request.FILES.get('imagen_serv_cuatro', None)
        contenido = request.POST.get('contenido', None)
        servicio_id = request.POST.get('servicio_id')

        # Validar los datos del formulario
        if not titulo:
            messages.error(request, 'El título es obligatorio.')
            return redirect('creador_post_serv')

        if not servicio_id:
            messages.error(request, 'Debe seleccionar un servicio.')
            return redirect('creador_post_serv')

        # Obtener el servicio seleccionado por el usuario
        servicio = Servicio_prov.objects.get(id=servicio_id)

        # Crear el nuevo post
        post = Post_prov.objects.create(
            titulo=titulo,
            archivo_contenido=contenido,
            user=request.user.profile_proveedor,
            servicio=servicio
        )


        # Guardar las imágenes en el almacenamiento en la nube
        if imagen_serv:
            image_path = f'{settings.PUBLIC_MEDIA_LOCATION}/{imagen_serv.name}'
            storage = GoogleCloudStorage()
            storage.save(image_path, imagen_serv)
            post.imagen_serv = image_path
        
        if imagen_serv_dos:
            image_path = f'{settings.PUBLIC_MEDIA_LOCATION}/{imagen_serv_dos.name}'
            storage = GoogleCloudStorage()
            storage.save(image_path, imagen_serv_dos)
            post.imagen_serv_dos = image_path
        
        if imagen_serv_tres:
            image_path = f'{settings.PUBLIC_MEDIA_LOCATION}/{imagen_serv_tres.name}'
            storage = GoogleCloudStorage()
            storage.save(image_path, imagen_serv_tres)
            post.imagen_serv_tres = image_path
        
        if imagen_serv_cuatro:
            image_path = f'{settings.PUBLIC_MEDIA_LOCATION}/{imagen_serv_cuatro.name}'
            storage = GoogleCloudStorage()
            storage.save(image_path, imagen_serv_cuatro)
            post.imagen_serv_cuatro = image_path



        post.save()

        messages.success(request, 'El post se ha creado correctamente.')
        return redirect('creador_post_serv')

    context = {
        'servicios': servicios,
        'post_list': post_list,
        'post': post, 

    }

    return render(request, 'proveedor/servicio_proveedor/crea_post_servicio.html', context)




#------------------------------- EDITAR POST -------------------------------------------
@login_required
@login_required(login_url='login_proveedor')
def editar_post(request, id):
    post_edit = get_object_or_404(Post_prov, id=id)

    if request.method == 'POST':
        # Obtener los datos del formulario
        imagen_serv_edit = request.FILES.get('imagen_serv', None)
        imagen_serv_dos_edit = request.FILES.get('imagen_serv_dos', None)
        imagen_serv_tres_edit = request.FILES.get('imagen_serv_tres', None)
        imagen_serv_cuatro_edit = request.FILES.get('imagen_serv_cuatro', None)
        contenido_edit = request.POST.get('archivo_contenido', None)

        # Asigna los valores existentes del modelo si no se proporcionan nuevos datos
        if not imagen_serv_edit:
            imagen_serv_edit = post_edit.imagen_serv
        if not imagen_serv_dos_edit:
            imagen_serv_dos_edit = post_edit.imagen_serv_dos
        if not imagen_serv_tres_edit:
            imagen_serv_tres_edit = post_edit.imagen_serv_tres
        if not imagen_serv_cuatro_edit:
            imagen_serv_cuatro_edit = post_edit.imagen_serv_cuatro
        if not contenido_edit:
            contenido_edit = post_edit.archivo_contenido

        # Actualiza los campos del modelo si se proporcionan nuevos datos
        if imagen_serv_edit != post_edit.imagen_serv or imagen_serv_dos_edit != post_edit.imagen_serv_dos or imagen_serv_tres_edit != post_edit.imagen_serv_tres or imagen_serv_cuatro_edit != post_edit.imagen_serv_cuatro or contenido_edit != post_edit.archivo_contenido:


            # Guardar las imágenes en el almacenamiento en la nube
          
            image_path = f'{settings.PUBLIC_MEDIA_LOCATION}/{imagen_serv_edit.name}'
            storage = GoogleCloudStorage()
            storage.save(image_path, imagen_serv_edit)
            post_edit.imagen_serv = image_path
        
           
            image_path = f'{settings.PUBLIC_MEDIA_LOCATION}/{imagen_serv_dos_edit.name}'
            storage = GoogleCloudStorage()
            storage.save(image_path, imagen_serv_dos_edit)
            post_edit.imagen_serv_dos = image_path
        
            
            image_path = f'{settings.PUBLIC_MEDIA_LOCATION}/{imagen_serv_tres_edit.name}'
            storage = GoogleCloudStorage()
            storage.save(image_path, imagen_serv_tres_edit)
            post_edit.imagen_serv_tres = image_path
        
            
            image_path = f'{settings.PUBLIC_MEDIA_LOCATION}/{imagen_serv_cuatro_edit.name}'
            storage = GoogleCloudStorage()
            storage.save(image_path, imagen_serv_cuatro_edit)
            post_edit.imagen_serv_cuatro = image_path


            post_edit.archivo_contenido = contenido_edit
            post_edit.save()


    context = {
        'editor': post_edit
    }


    return render(request, 'proveedor/servicio_proveedor/editar_post_serv.html', context)



#-----------------------Eliminar Post---------------------
@login_required
def eliminar_post_prov(request, id):
    post_delete = Post_prov.objects.get(id=id)
    post_delete.delete()
    return redirect('creador_post_serv')



#///////////////////////////////////////////////////////////////////////////////////
#//////////////////////// VISTAS DE SERVICIOS Y POSTS //////////////////////////////
#///////////////////////////////////////////////////////////////////////////////////

def vista_servicios(request):
    # Obtiene el usuario que está haciendo la petición
    user = request.user
    # Verifica si el usuario tiene un perfil de proveedor
    if hasattr(user, 'profile_proveedor'):
        # Si el usuario es un proveedor, se obtiene su perfil usando select_related()
        profile = user.profile_proveedor
    # Verifica si el usuario tiene un perfil de vendedor
    elif hasattr(user, 'profile_vendedor'):
        # Si el usuario es un vendedor, se obtiene su perfil usando select_related()
        profile = user.profile_vendedor
    else:
        # Si el usuario no tiene un perfil de proveedor o vendedor, lanza un error 404
        messages.success(request,"Este usuario no tiene un perfil de proveedor o vendedor.")
        

    # Obtiene todos los servicios relacionados con el perfil del usuario
    # usando all() y prefetch_related() para mejorar el rendimiento
    servicios = Servicio_prov.objects.filter(user=profile).prefetch_related('contactoProveedor_forenkey', 'ubicacionProveedor_forenkey', 'geoServiciosProveedor_forenkey')

    # Crea un diccionario de contexto con los servicios obtenidos
    context={
        'servicios': servicios
    }


    # Renderiza la plantilla 'proveedor/servicio_proveedor/vista_servicio.html' usando el diccionario de contexto
    return render(request, 'proveedor/servicio_proveedor/vista_servicio.html', context)







@login_required
def post_vista_list(request, slug):
    

    servicio = get_object_or_404(Servicio_prov, slug=slug)
    codigo_unico = servicio.user.codigo_unico_proveedor

    posts = servicio.post_prov_set.order_by('-fecha_creacion')
    
    context = {
        'servicio': servicio,
        'posts': posts,
        'codigo_unico': codigo_unico
    }


    return render(request, 'proveedor/servicio_proveedor/vista_post.html', context)





def detail_post(request, slug):
    post = get_object_or_404(Post_prov, slug=slug)
    context = {'posts': post}
    return render(request, 'proveedor/servicio_proveedor/detail_post.html', context)