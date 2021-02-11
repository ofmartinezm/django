from django.shortcuts import render
from django.http import HttpResponse,  Http404
from .models import Libro, Autor



# Create your views here.
def libros(request):
    libros=Libro.objects.all()
    data={'libros':libros}
    # data=dict(libros=libros)
    return render(request,'libros.html',data)

def libro_detail(request,libro_id):
    try:
        libro=Libro.objects.get(id = libro_id)
    except Libro.DoesNotExist:
        raise Http404(f'Libro con id = {libro_id} no existe!!')
        
    
    #  return HttpResponse(f'<h1>detalle del libro{libro_id}</h1>')  
    data= dict(libro=libro)
    return render(request, 'libro.html', data)

def autor_detail(request, autor_id ):
    try:
        autor= Autor.objects.get(id = autor_id)
        libros= Libro.objects.filter(autor__apellidos__contains=autor.apellidos)
    except Autor.DoesNotExist:
        raise Http404(f'El Autor = {autor_id} no existe!!')

    data={'autor': autor,'libros' : libros}
    return render(request, 'autor.html', data)