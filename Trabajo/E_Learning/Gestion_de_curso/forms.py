from django.shortcuts import render, redirect
from .forms import CursoForm  # Importa el formulario CursoForm
from .models import Curso

def crear_curso(request):
    if request.method == 'POST':
        form = CursoForm(request.POST, request.FILES)  # Crea una instancia de CursoForm con los datos POST
        if form.is_valid():  # Verifica si el formulario es válido
            form.save()  # Guarda el nuevo curso en la base de datos
            return redirect('lista_cursos')
    else:
        form = CursoForm()  # Crea una instancia vacía de CursoForm para el método GET

    return render(request, 'Gestion_de_curso/crear_curso.html', {'form': form})
