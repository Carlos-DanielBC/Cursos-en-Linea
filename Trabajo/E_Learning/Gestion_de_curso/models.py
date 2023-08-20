from django.db import models
# from inscriptions.models import Inscripcion

class Curso(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    nivel_dificultad = models.CharField(max_length=20)
    materiales_educativos = models.FileField(upload_to='materiales/')

    def __str__(self):
        return self.titulo

class User(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=100)
    correo = models.EmailField(max_length=200, unique=True)
    identidad = models.CharField(max_length=20)
    contraseña = models.CharField(max_length=300)
    
    def __str__(self):
        return self.nombre

class Comment(models.Model):
    nombre_user = models.CharField(max_length=200)
    identidad_user = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=1000)
    
    def __str__(self):
        return self.title