from django.shortcuts import render, redirect
from django.urls import reverse
from blog.models import Articulo
from blog.forms import ArticuloForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q
    


# Create your views here.
def listar_articulos(request):
    articulos= Articulo.objects.all()
    contexto = {
        'articulos': articulos
    }
    http_response= render(
        request=request,
        template_name='blog/lista_articulos.html',
        context= contexto,
    )
    return http_response


@login_required
def crear_articulo(request):
    if request.method == 'POST':
        form = ArticuloForm(request.POST)
        if form.is_valid():
            data= form.cleaned_data
            titulo= data["titulo"]
            subtitulo= data["subtitulo"]
            cuerpo= data["cuerpo"]
            autor= data["autor"]
            articulo= Articulo.objects.create(titulo=titulo, subtitulo= subtitulo, cuerpo= cuerpo, autor=autor)
            url_exitosa=reverse('lista_articulos')
            return redirect(url_exitosa)
    else:
        form = ArticuloForm()
    http_response= render(
        request= request, 
        template_name= 'blog/crear_articulo.html', 
        context= {'form': form},
        )
    return http_response

   
def buscar_articulos(request):
    if request.method == 'POST':
        data= request.POST
        busqueda= data['busqueda']
        articulos= Articulo.objects.filter(Q(titulo__icontains=busqueda)| Q(subtitulo__icontains=busqueda))
        contexto= {
            'articulos': articulos,
        }
        http_response= render(
            request= request, 
            template_name= 'blog/lista_articulos.html', 
            context=contexto,
        )
        return http_response
    else:
        return redirect('lista_articulos')


