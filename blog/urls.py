from django.contrib import admin
from django.urls import path
from blog.views import crear_articulo,listar_articulos, buscar_articulos, editar_articulo, eliminar_articulo, ver_articulo, about

urlpatterns = [
    path("crear/", crear_articulo, name='crear_articulo'),
    path("pages/", listar_articulos, name='lista_articulos'),
    path("buscar/", buscar_articulos, name='buscar_articulos'),
    path("editar/<int:id>/", editar_articulo, name='editar_articulo'),
    path("eliminar/<int:id>/", eliminar_articulo, name='eliminar_articulo'),
    path("pages/page<int:id>/", ver_articulo, name='ver_articulo'),
    path("about/", about, name= 'about'),
]
