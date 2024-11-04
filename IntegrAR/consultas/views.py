from django.shortcuts import render, redirect, get_object_or_404
from .models import Consulta, Categoria, ConsultaEspecifica, Ubicacion, Area, Mensaje
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import RegistroForm, NuevaConsultaEspecifica, MensajeForm, ResponderMensajeForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponseForbidden
from django.contrib.auth.models import User, Group

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('inicio')  # Redirige a la página de inicio después de iniciar sesión
        else:
            messages.error(request, 'Usuario o contraseña incorrectos')
    return render(request, 'login.html')

def is_sjm(user):
    return user.groups.filter(name='SJM').exists()

def is_sjmA(user):
    return user.groups.filter(name='SJM-admin').exists()

def inicio(request):
    # Obtiene la categoría "Noticias"
    categoria_noticias = Categoria.objects.get(nombre="Noticias")
    
    # Filtra consultas por la categoría "Noticias"
    consultas_noticias = Consulta.objects.filter(categoria=categoria_noticias)

    return render(request, 'inicio.html', {'consultas': consultas_noticias})


def salud(request, categoria_id=None):
    # Obtiene la categoría "Salud"
    categoria_salud = Categoria.objects.get(nombre="Salud")
    
    # Filtra consultas por la categoría "Noticias"
    consultas_salud = Consulta.objects.filter(categoria=categoria_salud)

    return render(request, 'salud.html', {'consultas': consultas_salud})

def educacion(request, categoria_id=None):
    # Obtiene la categoría "Salud"
    categoria_educacion = Categoria.objects.get(nombre="Educacion")
    
    # Filtra consultas por la categoría "Noticias"
    consultas_educacion = Consulta.objects.filter(categoria=categoria_educacion)

    return render(request, 'educacion.html', {'consultas': consultas_educacion})

def tramites(request, categoria_id=None):
    # Obtiene la categoría "Salud"
    categoria_tramites = Categoria.objects.get(nombre="Tramites")
    
    # Filtra consultas por la categoría "Noticias"
    consultas_tramites = Consulta.objects.filter(categoria=categoria_tramites)

    return render(request, 'tramites.html', {'consultas': consultas_tramites})

def capacitaciones(request):
    
    return render(request, 'capacitaciones.html')

def presencial(request, categoria_id=None):
    # Obtiene la categoría "Salud"
    categoria_presencial = Categoria.objects.get(nombre="Capacitacion Presencial")
    
    # Filtra consultas por la categoría "Noticias"
    consultas_presencial = Consulta.objects.filter(categoria=categoria_presencial)

    return render(request, 'capacitacion_presencial.html', {'consultas': consultas_presencial})

def semipresencial(request, categoria_id=None):
    # Obtiene la categoría "Salud"
    categoria_semipresencial = Categoria.objects.get(nombre="Capacitacion Semi Presencial")
    
    # Filtra consultas por la categoría "Noticias"
    consultas_semipresencial = Consulta.objects.filter(categoria=categoria_semipresencial)

    return render(request, 'capacitacion_semipresencial.html', {'consultas': consultas_semipresencial})

def virtual(request, categoria_id=None):
    # Obtiene la categoría "Salud"
    categoria_virtual = Categoria.objects.get(nombre="Capacitacion Virtual")
    
    # Filtra consultas por la categoría "Noticias"
    consultas_virtual = Consulta.objects.filter(categoria=categoria_virtual)

    return render(request, 'capacitacion_virtual.html', {'consultas': consultas_virtual})

@login_required
@user_passes_test(is_sjm)
def crear_consulta(request):
    categorias = Categoria.objects.all()
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        descripcion = request.POST.get('descripcion')
        enlace = request.POST.get('enlace')
        categoria_id = request.POST.get('categoria')
        categoria = get_object_or_404(Categoria, id=categoria_id)
        Consulta.objects.create(titulo=titulo, descripcion=descripcion, enlace=enlace, categoria=categoria)
        return redirect('crear_consulta')
    return render(request, 'crear_consulta.html', {'categorias': categorias})

def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Iniciar sesión automáticamente después de registrarse
            return redirect('inicio')  # Redirigir a la página de inicio o donde prefieras
    else:
        form = RegistroForm()
    return render(request, 'registro.html', {'form': form})

@login_required
@user_passes_test(is_sjmA)
def administrar_usuarios(request):
    users = User.objects.all()
    groups = Group.objects.all()

    if request.method == 'POST':
        user_id = request.POST.get('user')
        group_id = request.POST.get('group')
        action = request.POST.get('action')  # Captura la acción (asignar o eliminar)

        user = User.objects.get(id=user_id)
        group = Group.objects.get(id=group_id)

        if action == 'add':
            # Asigna el grupo al usuario
            user.groups.add(group)
            messages.success(request, f"El grupo '{group.name}' ha sido asignado a {user.username}")
        
        elif action == 'remove':
            # Elimina el grupo del usuario
            user.groups.remove(group)
            messages.success(request, f"El grupo '{group.name}' ha sido removido de {user.username}")

        return redirect('administrar_usuarios')  # Redirige para evitar duplicados al recargar

    context = {
        'users': users,
        'groups': groups,
    }
    return render(request, 'administrar_usuarios.html', context)

@login_required
@user_passes_test(is_sjm)
def crear_consulta_especifica(request):
    if request.method == 'POST':
        form = NuevaConsultaEspecifica(request.POST)
        if form.is_valid():
            form.save()
            return redirect('filtrar_consultas')
    else:
        form = NuevaConsultaEspecifica()
    return render(request, 'crear_consulta_especifica.html', {'form': form})

def filtrar_consultas(request):
    consultas = ConsultaEspecifica.objects.all()
    ubicaciones = Ubicacion.objects.all()
    areas = Area.objects.all()

    selected_ubicacion = request.GET.get('ubicacion')
    selected_area = request.GET.get('area')

    if selected_ubicacion:
        consultas = consultas.filter(ubicacion__id=selected_ubicacion)

    if selected_area:
        consultas = consultas.filter(area__id=selected_area)

    return render(request, 'filtrar_consultas.html', {
        'consultas': consultas,
        'ubicaciones': ubicaciones,
        'areas': areas,
        'selected_ubicacion': selected_ubicacion,
        'selected_area': selected_area,
    })

def enviar_mensaje(request):
    if request.method == 'POST':
        form = MensajeForm(request.POST)
        if form.is_valid():
            mensaje = form.save(commit=False)
            if request.user.is_authenticated:
                mensaje.usuario = request.user  # Asignar el usuario autenticado
                mensaje.nombre = ""
                mensaje.apellido = ""
                mensaje.telefono = ""
                mensaje.email = ""
                mensaje.nucleo_familiar = ""
            mensaje.save()
            return redirect('/')  # Redirigir a una página de éxito
    else:
        form = MensajeForm()

    return render(request, 'enviar_mensaje.html', {'form': form})

@login_required
@user_passes_test(is_sjm)
def gestionar_mensajes(request):
    if not request.user.groups.filter(name='SJM').exists():
        return redirect('inicio')  # Redirigir si no es SJM

    mensajes = Mensaje.objects.all()

    if request.method == 'POST':
        mensaje_id = request.POST.get('mensaje_id')
        mensaje = get_object_or_404(Mensaje, id=mensaje_id)

        form = ResponderMensajeForm(request.POST, instance=mensaje)
        if form.is_valid():
            form.save()  # Esto guarda la ubicación, área y respuesta al mensaje
            return redirect('gestionar_mensajes')  # Redirigir después de guardar

    return render(request, 'gestionar_mensajes.html', {'mensajes': mensajes})

@login_required
def mis_consultas(request):
    if request.user.is_authenticated:
        mensajes = Mensaje.objects.filter(usuario=request.user)
    else:
        mensajes = []

    return render(request, 'mis_consultas.html', {'mensajes': mensajes})