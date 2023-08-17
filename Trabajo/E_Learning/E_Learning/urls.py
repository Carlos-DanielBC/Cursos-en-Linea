from django.contrib import admin
from django.urls import path, include
# from Gestion_de_curso import views  # Importa las vistas de tu aplicación

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('lista_cursos/', views.lista_cursos, name='lista_cursos'),  # Ruta para la lista de cursos
    # path('crear_curso/', views.crear_curso, name='crear_curso'),  # Ruta para crear un curso
]

urlpatterns += [
    path('', include('Gestion_de_curso.urls')),
]