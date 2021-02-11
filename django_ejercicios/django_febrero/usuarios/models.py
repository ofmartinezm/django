from django.db import models

# Create your models here.

class Usuario(models.Model):
    GENEROS= [('H','Hombre'),('F','Mujer'),('O','Otros')]
    username = models.CharField(max_length=100)
    mail =  models.EmailField(max_length=50)
    gender = models.CharField(max_length=1, choices=GENEROS)

