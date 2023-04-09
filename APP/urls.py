from django.urls import path
from .views import *


urlpatterns = [
    
    path("", inicioApp, name="inicioApp"),
    path("publications/", publications, name="publications"),
    # path("crear_curso/", crear_curso),
    # path("cursos/", cursos, name="cursos"),
    # path("publications/", publications, name="publications"),
    # path("estudiantes/", estudiantes, name="estudiantes"),
    # path("entregables/", entregables, name="entregables"),
    
    
] #path("publications/", publications, name="publications"),