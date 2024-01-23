from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import UpdateView, DeleteView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import redirect
from django.utils.decorators import method_decorator
from appfranco.models import Libros, VideoJuegos, Peliculas
from appfranco.forms import UserRegistrationForm, UserEditForm

def index(request):
    return render(request, "index.html")

def about_me(request):
    return render(request, 'about_me.html')

def admin(request):
    return redirect('/admin/')

# Comprobacion de admin

def es_admin(user):
    return user.is_authenticated and user.is_superuser

# Lectura, busqueda e ingreso de datos

@login_required
def add_video_juegos(request):

    if not request.user.is_superuser:
        return redirect('index.html')

    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        desarrolladora = request.POST.get('desarrolladora')
        stock = request.POST.get('stock')

        videoJuego = VideoJuegos(nombre = nombre, desarrolladora = desarrolladora, stock = stock)

        videoJuego.save()

    return render (request, "videoJuegos.html")

@login_required
def add_libros(request):

    if not request.user.is_superuser:
        return redirect('index.html')

    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        autor = request.POST.get('autor')
        stock = request.POST.get('stock')

        libro = Libros(nombre = nombre, autor = autor, stock = stock)

        libro.save()

    return render (request, "libros.html")


@login_required
def add_peliculas(request):

    if not request.user.is_superuser:
        return redirect('index.html')

    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        director = request.POST.get('director')
        stock = request.POST.get('stock')

        pelicula = Peliculas(nombre = nombre, director = director, stock = stock)

        pelicula.save()

    return render (request, "peliculas.html")

# Vistas de búsqueda

@login_required
def busqueda_video_juegos(request):

    return render (request, 'busquedaVideoJuegos.html')

@login_required
def busqueda_libros(request):

    return render (request, 'busquedaLibros.html')

@login_required
def busqueda_peliculas(request):

    return render (request, 'busquedaPeliculas.html')

# Vistas de resultados

@login_required
def resultados_video_juegos(request):

    if request.method == "GET":

        nombre = request.GET.get('nombre')

        if nombre is None:
            return HttpResponse('Enviar el nombre')
        
        videoJuegos = VideoJuegos.objects.filter(nombre__icontains=nombre)

        contexto = {
            "videoJuegos": videoJuegos,
            "nombre": nombre
        }

        return render (request, 'resultadosVideoJuegos.html', contexto)

@login_required
def resultados_libros(request):

    if request.method == "GET":

        nombre = request.GET.get('nombre')

        if nombre is None:
            return HttpResponse('Enviar el nombre')
        
        libros = Libros.objects.filter(nombre__icontains=nombre)

        contexto = {
            "libros": libros,
            "nombre": nombre
        }

        return render (request, 'resultadosLibros.html', contexto)

@login_required
def resultados_peliculas(request):

    if request.method == "GET":

        nombre = request.GET.get('nombre')

        if nombre is None:
            return HttpResponse('Enviar el nombre')
        
        peliculas = Peliculas.objects.filter(nombre__icontains=nombre)

        contexto = {
            "peliculas": peliculas,
            "nombre": nombre
        }

        return render (request, 'resultadosPeliculas.html', contexto)
    
# Vista de lectura

@login_required
def leer_video_juegos(request):

    video_juegos = VideoJuegos.objects.all()

    contexto = {"video_juegos": video_juegos}

    return render ( request, "leer_video_juegos.html", contexto)

@login_required
def leer_libros(request):

    libros = Libros.objects.all()

    contexto = {"libros": libros}

    return render ( request, "leer_libros.html", contexto)

@login_required
def leer_peliculas(request):

    peliculas = Peliculas.objects.all()

    contexto = {"peliculas": peliculas}

    return render ( request, "leer_peliculas.html", contexto)

# Métodos por clases

class VideoJuegosUpdate(UpdateView):
    
    model = VideoJuegos
    fields = ['nombre', 'desarrolladora', 'stock']
    template_name = 'updateVideoJuegos.html'
    success_url = '/video_juegos/'

    @method_decorator(user_passes_test(es_admin))
    def dispatch(self, *args, **kwargs):
        return super(VideoJuegosUpdate, self).dispatch(*args, **kwargs)

class VideoJuegosDelete(DeleteView):
    
    model= VideoJuegos
    template_name = 'videoJuegosConfirmDelete.html'
    success_url = '/video_juegos/'

    @method_decorator(user_passes_test(es_admin))
    def dispatch(self, *args, **kwargs):
        return super(VideoJuegosDelete, self).dispatch(*args, **kwargs)

class LibrosUpdate(UpdateView):
    
    model = Libros
    fields = ['nombre', 'autor', 'stock']
    template_name = 'updateLibros.html'
    success_url = '/libros/'

    @method_decorator(user_passes_test(es_admin))
    def dispatch(self, *args, **kwargs):
        return super(LibrosUpdate, self).dispatch(*args, **kwargs)

class LibrosDelete(DeleteView):
    
    model= Libros
    template_name = 'librosConfirmDelete.html'
    success_url = '/libros/'

    @method_decorator(user_passes_test(es_admin))
    def dispatch(self, *args, **kwargs):
        return super(LibrosDelete, self).dispatch(*args, **kwargs)

class PeliculasUpdate(UpdateView):
    
    model = Peliculas
    fields = ['nombre', 'director', 'stock']
    template_name = 'updatePeliculas.html'
    success_url = '/peliculas/'

    @method_decorator(user_passes_test(es_admin))
    def dispatch(self, *args, **kwargs):
        return super(PeliculasUpdate, self).dispatch(*args, **kwargs)

class PeliculasDelete(DeleteView):
    
    model= Peliculas
    template_name = 'peliculasConfirmDelete.html'
    success_url = '/peliculas/'

    @method_decorator(user_passes_test(es_admin))
    def dispatch(self, *args, **kwargs):
        return super(PeliculasDelete, self).dispatch(*args, **kwargs)

# Login y Registro
    
def login_request(request):
    mensaje = ""

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return render(request, 'index.html')
            else:
                mensaje = "Nombre de usuario o contraseña incorrecta."
        else:
            mensaje = "Datos inválidos. Por favor, intenta de nuevo."

    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {"form": form, "mensaje": mensaje})


def register_request(request):

    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            form.save()
            return render(request, 'registroExitoso.html', {'mensaje': f'El usuario {username} fue registrado con exito'})
        else:
             return render(request, 'registro.html', {'form': form})
    else:
        form = UserRegistrationForm()
        return render(request, 'registro.html', {'form': form})
    
@login_required
def editar_perfil(request): 

    usuario = request.user

    if request.method == 'POST':
        form = UserEditForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data

            usuario.username = data.get('username')
            usuario.email = data.get('email')
            usuario.password1 = data.get('password1')
            usuario.password2 = data.get('password2')
            usuario.first_name = data.get('first_name')
            usuario.last_name = data.get('last_name')

            usuario.save()

            return render(request, 'index.html')

    else:
        form = UserEditForm(initial={'email':usuario.email})
        return render(request, 'editar_perfil.html', {'form': form, 'usuario': usuario})   