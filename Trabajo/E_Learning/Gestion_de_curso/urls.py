from django.urls import path
from . import views

urlpatterns = [
    path('lista/', views.lista_cursos, name='lista_cursos'),
    path('crear_curso/', views.crear_curso, name='crear_curso'),
    path('home/', views.home)
]
