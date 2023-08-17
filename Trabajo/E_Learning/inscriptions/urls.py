from django.urls import path, include
from . import views

urlpatterns = [
    path('inscribirse/', views.inscribirse, name='inscribirse'),
    path('inscribirse/inscripcion_exitosa.html', views.inscripcion_exitosa, name='inscripcion-exitosa')
]