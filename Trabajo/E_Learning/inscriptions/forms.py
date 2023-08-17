from django import forms
from .models import Inscripcion

class InscripcionForm(forms.ModelForm):
    
    class Meta:
        model = Inscripcion
        fields = ['nombre', 'correo', 'telefono', 'evento']
