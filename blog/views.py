from django.shortcuts import render

# Create your views here.
def lista_articulos(request):
    contexto={
        'articulos': Articulo.objects.all()
    }
    http_response= render(
        request=request,
        template_name='blog/lista_articulos.html',
        context=contexto,
    )
    return http_response
