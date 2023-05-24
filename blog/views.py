from django.shortcuts import render, redirect
from django.urls import reverse
from blog.models import Articulo
from blog.forms import ArticuloForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q
    


# Create your views here.

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
            url_exitosa=reverse('lista_articulos') #redirecciono a la lista de articulos
            return redirect(url_exitosa)
    else:
        form = ArticuloForm()
    http_response= render(
        request= request, 
        template_name= 'blog/crear_articulo.html', 
        context= {'form': form},
        )
    return http_response



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



def ver_articulo(request, id):
    articulo= Articulo.objects.get(id= id)  # Obtener el artículo por su ID
    contexto = {
        'articulo': articulo
    }
    return render(
        request= request,
        template_name= 'blog/detalle_articulos.html', 
        context=contexto,
    )



@login_required
def editar_articulo(request, id): 
    articulo= Articulo.objects.get(id= id)
    if request.method=="POST":
        form= ArticuloForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            articulo.titulo= data["titulo"]
            articulo.subtitulo= data["subtitulo"]
            articulo.cuerpo= data["cuerpo"]
            articulo.autor= data["autor"]
            articulo.save()
            return redirect('lista_articulos') 
    else:
        inicial={
            'titulo': articulo.titulo,
            'subtitulo': articulo.subtitulo,
            'cuerpo': articulo.cuerpo,
            'autor': articulo.autor,
        }
        form= ArticuloForm(initial= inicial)
    return render(
        request=request,
        template_name= 'blog/crear_articulo.html',
        context={'form': form},
    )



@login_required
def eliminar_articulo(request, id): #pasamos id como argumento para saber que articulo es
    articulo= Articulo.objects.get(id= id)
    if request.method=="POST":
        articulo.delete() #borra el articulo
        url_exitosa=reverse('lista_articulos') #manda a url_exitosa donde ya no esta ese articulo
        return redirect(url_exitosa)
    else:
        contexto= {
            'articulo': articulo
        }
        http_response= render(
            request= request, 
            template_name= 'blog/articulo_confirm_delete.html', 
            context=contexto,
        )
        return http_response
    
  


