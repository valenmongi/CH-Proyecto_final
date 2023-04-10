from django.urls import path
from .views import *


urlpatterns = [
    
    path("", index, name="index"),
    path("publications/", publications, name="publications"),
    path("users/", users, name="users"),
    # path("crear_curso/", crear_curso),
    # path("cursos/", cursos, name="cursos"),
    # path("publications/", publications, name="publications"),
    # path("estudiantes/", estudiantes, name="estudiantes"),
    # path("entregables/", entregables, name="entregables"),
    
    
] #path("publications/", publications, name="publications"), 