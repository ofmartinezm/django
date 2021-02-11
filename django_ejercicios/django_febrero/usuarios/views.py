from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserForm , UserFornM

# Create your views here.


def usuarios(request):
    data = {}
    if request.method == 'POST':
        filled_form = UserFornM(request.POST)
        if filled_form.is_valid():
            user = filled_form.save()
            data = {'user': user}
    return render(request, 'usuarios.html', data)

def add_users1(request):
    return render(request,'add_users1.html')

def add_users2(request):
    data = {'forms' : UserForm()}
    return render(request,'add_users2.html', data)     

def add_users3(request):
    data = {'forms' : UserFornM()}
    return render(request,'add_users3.html', data)     