from django.shortcuts import render, redirect
# from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
# from django.http import HttpResponse
from django.contrib.auth.hashers import make_password
from .models import Curso

def Login(request):
    return render(request, 'login.html')

def register(request):
    if request.method == 'GET':
        print('enviando formulario')
    else:
        try:
            nuevo_usuario = User(
                username = request.POST['nombre'],
                last_name = request.POST['apellido'],
                email = request.POST['correo'],
                first_name = request.POST['identidad'],
                password =  make_password(request.POST['contraseña']),
            )
            nuevo_usuario.save()
            login(request, nuevo_usuario)
            return redirect('home')
        except IntegrityError:
            return render(request, 'Users/User_signUp.html', {
                "error": 'User already exists'
            })
    return render(request, 'Users/User_signUp.html', {
        "error": 'Password do not match'
    })


def close_sesion(request):
    logout(request)
    return redirect('sesion')

def sesion(request):
    if request.method == 'GET':
        return render(request, 'Users/User_signIn.html')
    else:
        nombre = request.POST['nombre']
        contraseña = request.POST['contraseña']

        user = authenticate(request, username=nombre, password=contraseña)

        if user is None:
            return render(request, 'Users/User_signIn.html', {
                "error": 'Nombre de usuario o contraseña incorrecta'
            })
        else:
            login(request, user)
            return redirect('home')
        
        

def home(request):
    return render(request, 'home.html')


def lista_cursos(request):
    cursos = Curso.objects.all()
    return render(request, 'Gestion_de_curso/lista_cursos.html', {'cursos': cursos})




def crear_curso(request):
    if request.method == 'POST':
        nuevo_curso = Curso(
            titulo=request.POST['titulo'],
            descripcion=request.POST['descripcion'],
            nivel_dificultad=request.POST['nivel_dificultad'],  # Corregido el nombre del campo
            materiales_educativos=request.FILES['materiales_educativos']
        )
        nuevo_curso.save()
        return redirect('lista_cursos')
    return render(request, 'Gestion_de_curso/crear_curso.html')
