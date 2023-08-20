from django.shortcuts import render, redirect
# from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
# from django.http import HttpResponse
from django.contrib.auth.hashers import make_password
from .models import Curso
from .models import Comment

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
    # Verifica si el usuario está autenticado
    if request.user.is_authenticated:
        # El usuario está autenticado, obten el first_name
        username = request.user.username
        first_name = request.user.first_name

        if request.method == 'POST':
            # Obtiene el título y el comentario del formulario
            title = request.POST['title']
            comment_text = request.POST['comment']

            # Crea y guarda el comentario en la base de datos junto con el primer nombre del usuario
            comentario = Comment(nombre_user= username,identidad_user=first_name, title=title, description=comment_text)
            comentario.save()
            return redirect('home')
        else:
            datos = Comment.objects.all()
            return render(request, 'home_grafic.html', {'datos': datos})
            # Redirige a donde desees después de guardar el comentario
    
    return render(request, 'home_grafic.html')


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


def obtener_datos_grafico(request):
    # Obtener el número de usuarios con first_name igual a "estudiante" y "maestro"
    estudiantes = User.objects.filter(first_name="estudiante").count()
    maestros = User.objects.filter(first_name="maestro").count()

    # Crear un diccionario con los datos
    data = {
        "Todos": estudiantes + maestros,  # Puedes ajustar esto según tu lógica
        "Estudiantes": estudiantes,
        "Maestros": maestros,
         # Puedes ajustar esto según tu lógica
    }

    return JsonResponse(data)