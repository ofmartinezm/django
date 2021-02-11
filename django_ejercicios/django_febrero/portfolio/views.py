from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def portfolio(request):
   # return HttpResponse('<h1> portfolio... Hola mundo desde DJANGO!!</H1>')
   autor = 'Alejandro Cerezo'
   correo = 'alce65@hotmail.es'
   return render(request,'portfolio.html',{
       'autor' : autor,
       'correo' : correo
   
   })

def home(request):
    return render(request, 'home.html')



