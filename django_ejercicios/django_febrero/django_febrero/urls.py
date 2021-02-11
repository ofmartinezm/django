"""django_febrero URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import portfolio.views
import libros.views


import usuarios.views



from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('portfolio/', portfolio.views.portfolio,name='portfolio' ),
    path('', portfolio.views.home,name='home' ),
    path('libros/',libros.views.libros, name = 'libros' ),
    path('libros/<int:libro_id>',libros.views.libro_detail, name = 'libro' ),
    path('autor/<int:autor_id>',libros.views.autor_detail, name = 'autor' ),
    path('usuarios/',usuarios.views.usuarios, name = 'usuarios' ),
    path('add_users1/',usuarios.views.add_users1, name = 'add_users1' ),
    path('add_users2/',usuarios.views.add_users2, name = 'add_users2' ),
    path('add_users3/',usuarios.views.add_users3, name = 'add_users3' ),

]

