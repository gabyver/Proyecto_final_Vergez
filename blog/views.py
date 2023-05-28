from django.shortcuts import render, redirect
from django.urls import reverse
from blog.models import Articulo
from blog.forms import ArticuloForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.
def about(request):
    contexto = {
        'nombre': 'Gabriela',
        'edad': 42,
        'pais': 'Argentina',
        'profesion': 'Ingeniera en Telecomunicaciones',
        'titulo': 'Sobre mí',
        'descripcion': 'Soy secretaria en una escuela primaria, me gustan las manualidades, empecé el curso de Python por una amiga que me insistió, me gusta pero tengo que dedicar mucho tiempo y a veces con mis hijas y trabajo, no puedo.',
    }

    return render(
        request=request,
        template_name= 'blog/about.html',
        context=contexto,
    )


@login_required
def crear_articulo(request):
    if request.method == 'POST':
        form = ArticuloForm(request.POST, request.FILES)
        if form.is_valid():
            articulo= form.save()
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
    articulo = Articulo.objects.get(id=id)

    if request.user != articulo.autor:
        messages.error(request, "No tienes permiso para editar este artículo.")
        return redirect('lista_articulos')
    
    if request.method == "POST":
        form = ArticuloForm(request.POST, request.FILES, instance=articulo)
        if form.is_valid():
            articulo.titulo = form.cleaned_data['titulo']
            articulo.subtitulo = form.cleaned_data['subtitulo']
            articulo.cuerpo = form.cleaned_data['cuerpo']
            if 'imagen' in form.cleaned_data:
                articulo.imagen = form.cleaned_data['imagen']
                form.save()
                messages.success(request, "Artículo editado correctamente.")
                return redirect('lista_articulos')
            else:
                messages.error(request, "Error al editar el artículo.")
        else:
            return render(
                request= request,
                template_name= 'blog/editar_articulo.html',
                context= {
                    'form': form,
                    'articulo': articulo
                }
            )

    else:
        form = ArticuloForm(instance=articulo)
        return render(
            request= request,
            template_name= 'blog/editar_articulo.html',
            context= {
                'form': form,
                'articulo': articulo
            }
        )
    
       
        


@login_required
def eliminar_articulo(request, id): #pasamos id como argumento para saber que articulo es
    articulo= Articulo.objects.get(id= id)

    if articulo.autor != request.user:  # Verificar si el usuario no es el autor del artículo
        messages.add_message(request, messages.ERROR, "No puedes eliminar este artículo porque no es tuyo.", extra_tags=str(articulo.id))
        return redirect('lista_articulos')
    
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
    
  


