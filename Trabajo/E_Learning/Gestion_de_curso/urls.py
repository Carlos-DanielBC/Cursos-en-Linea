from django.urls import path
from . import views
from django.views.generic import RedirectView

urlpatterns = [
    path('lista/', views.lista_cursos, name='lista_cursos'),
    path('crear_curso/', views.crear_curso, name='crear_curso'),
    path('', RedirectView.as_view(url='/Login/')),
    path('Login/', views.Login),
    path('Register/', views.register, name='register'),
    path('Sesion/', views.sesion, name='sesion'),
    path('logout/', views.close_sesion, name='logout'),
    path('home/', views.home, name='home'),
    path('obtener-datos-grafico/', views.obtener_datos_grafico, name='obtener_datos_grafico'),
]
