from django.contrib import admin
from django.urls import path
from blog.views import listar_articulos

urlpatterns = [
    path('articulos/', listar_articulos, name="lista_articulos"),
]
