from django.shortcuts import render, redirect
from django.urls import reverse
from blog.models import Articulo

# Create your views here.
def listar_articulos(request):
    contexto={
        'articulos': Articulo.objects.all()
    }
    http_response= render(
        request=request,
        template_name='blog/lista_articulos.html',
        context= {'articulos': Articulo},
    )
    return http_response
