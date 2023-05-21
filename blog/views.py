from django.shortcuts import render

# Create your views here.
def listar_articulos(request):
    contexto={
        'articulos': [
            {'titulo': 'Primer viaje', 'subtitulo': 'Viaje a Europa', 'cuerpo': 'Viaje en familia a Europa con promo aérea', 'autor': 'Gabriela', 'fecha_publicacion': '2023-05-21'},
        ]
    }
    http_response= render(
        request=request,
        template_name='blog/lista_articulos.html',
        context=contexto,
    )
    return http_response
