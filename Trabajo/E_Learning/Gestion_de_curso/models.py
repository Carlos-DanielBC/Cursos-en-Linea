from django.db import models

class Curso(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    nivel_dificultad = models.CharField(max_length=20)
    materiales_educativos = models.FileField(upload_to='materiales/')

    def __str__(self):
        return self.titulo
