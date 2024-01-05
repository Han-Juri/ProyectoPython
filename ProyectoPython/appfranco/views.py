from django.shortcuts import render
from django.http import HttpResponse
from appfranco.models import Libros, VideoJuegos, Peliculas

def index(request):
    return render(request, "index.html")


def video_juegos(request):

    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        desarrolladora = request.POST.get('desarrolladora')
        stock = request.POST.get('stock')

        videoJuego = VideoJuegos(nombre = nombre, desarrolladora = desarrolladora, stock = stock)

        videoJuego.save()

    return render (request, "videoJuegos.html")


def libros(request):

    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        autor = request.POST.get('autor')
        stock = request.POST.get('stock')

        libro = Libros(nombre = nombre, autor = autor, stock = stock)

        libro.save()

    return render (request, "libros.html")


def peliculas(request):

    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        director = request.POST.get('director')
        stock = request.POST.get('stock')

        pelicula = Peliculas(nombre = nombre, director = director, stock = stock)

        pelicula.save()

    return render (request, "peliculas.html")

# Vistas de búsqueda

def busqueda_video_juegos(request):

    return render (request, 'busquedaVideoJuegos.html')


def busqueda_libros(request):

    return render (request, 'busquedaLibros.html')


def busqueda_peliculas(request):

    return render (request, 'busquedaPeliculas.html')

#V istas de resultados

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
    
def leer_video_juegos(request):

    video_juegos = VideoJuegos.objects.all()

    contexto = {"video_juegos": video_juegos}

    return render ( request, "leer_video_juegos.html", contexto)


def leer_libros(request):

    libros = Libros.objects.all()

    contexto = {"libros": libros}

    return render ( request, "leer_libros.html", contexto)


def leer_peliculas(request):

    peliculas = Peliculas.objects.all()

    contexto = {"peliculas": peliculas}

    return render ( request, "leer_peliculas.html", contexto)