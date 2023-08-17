from django.shortcuts import render, redirect
from .models import Curso

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
