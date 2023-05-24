from django.contrib import admin
from django.urls import path
from blog.views import crear_articulo,listar_articulos, buscar_articulos, eliminar_articulo, editar_articulo

urlpatterns = [
    path("crear/", crear_articulo, name='crear_articulo'),
    path("articulos/", listar_articulos, name='lista_articulos'),
    path("buscar/", buscar_articulos, name='buscar_articulos'),
    path("eliminar/<int:id>/", eliminar_articulo, name='eliminar_articulo'),
    path("editar/<int:id>/", editar_articulo, name='editar_articulo'),
]
