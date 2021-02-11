from django.contrib import admin
from .models import Libro, Autor
# Register your models here.

@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'descripcion','genero','anio']   

@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ['apellidos', 'nombre','fecha_nacimiento']   
