from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse


def inicio(request):
    contexto= {}
    http_response= render(
        request= request,
        template_name = "blog/index.html",
        context=contexto,
    )
    return http_response


def saludar(request):
    saludo = "Hola querido usuario"
    pagina_html = HttpResponse(saludo)
    return pagina_html


def saludar_con_html(request):
    contexto={}
    http_response= render(
        request= request,
        template_name='blog/base.html',
        context=contexto,
    )
    return http_response
