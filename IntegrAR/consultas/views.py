from django.shortcuts import render, redirect, get_object_or_404
from .models import Consulta, Categoria
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import RegistroForm

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

def crear_consulta(request):
    categorias = Categoria.objects.all()
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        descripcion = request.POST.get('descripcion')
        categoria_id = request.POST.get('categoria')
        categoria = get_object_or_404(Categoria, id=categoria_id)
        Consulta.objects.create(titulo=titulo, descripcion=descripcion, categoria=categoria)
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
