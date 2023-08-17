from django.db import models

# Create your models here.
class Inscripcion(models.Model):
    
    nombre = models.CharField(max_length=30)
    correo = models.CharField(max_length=50)
    telefono = models.CharField(max_length=12)
    evento = models.BooleanField()