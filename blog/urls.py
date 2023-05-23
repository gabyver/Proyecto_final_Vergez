from django.contrib import admin
from django.urls import path
from blog.views import listar_articulos, crear_articulo, buscar_articulos

urlpatterns = [
    path("articulos/", listar_articulos, name="lista_articulos"),
    path("crear/", crear_articulo, name='crear_articulo'),
    path("buscar/", buscar_articulos, name='buscar_articulos'),
]
