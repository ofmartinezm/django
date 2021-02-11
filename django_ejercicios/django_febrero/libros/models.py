from django.db import models

# Create your models here.
class Libro(models.Model):
    GENEROS = [(1,'NOVELA'), (2,'ENSAYO')]
    titulo = models.CharField(max_length=100)
    autor = models.ManyToManyField('Autor', blank=True)
    anio = models.CharField(max_length=10)
    lugar_edicion = models.CharField(max_length=100)
    anio_edicion = models.CharField(max_length=10)
    editorial = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True) 
    genero = models.IntegerField(choices=GENEROS,blank=True)
    portada = models.ImageField(upload_to="static/images_db")
    def __str__(self):
        return f'{self.titulo}  {self.descripcion} {self.genero}'
    
class Autor(models.Model):
    apellidos = models.CharField(max_length= 100)
    nombre = models.CharField(max_length=100, blank=True)
    fecha_nacimiento = models.DateField(null=True,blank=True)
    lugar_nacimiento = models.CharField(max_length=100, blank=True)
    def __str__(self):
        return f'{self.nombre} {self.apellidos} {self.fecha_nacimiento}'




