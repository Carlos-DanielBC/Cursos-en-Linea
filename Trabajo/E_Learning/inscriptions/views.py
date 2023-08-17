from django.shortcuts import render, redirect

# Create your views here.
from .models import Inscripcion
from .forms import InscripcionForm

def inscribirse(request):
    if request.method == 'POST':
        form = InscripcionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inscripcion_exitosa.html')  # Redirigir a una página de éxito
    else:
        form = InscripcionForm()
    
    return render(request, 'inscripcion_form.html', {'form': form})

def inscripcion_exitosa(request):

    return render(request, 'inscripcion_exitosa.html')