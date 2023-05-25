from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LogoutView
from django.contrib.auth import login, authenticate
from perfiles.forms import UserRegisterForm 

# Create your views here.
def registro(request):
    if request.method=="POST":
        formulario= UserRegisterForm(request.POST)

        if formulario.is_valid():
            formulario.save()
            url_exitosa= reverse('inicio')
            return redirect(url_exitosa)
        
    else:
        formulario=UserRegisterForm()
    
    return render(
        request=request,
        template_name='perfiles/registro.html',
        context={'form':formulario}
        )
    

def login_view(request):
    next_url = request.GET.get('next')
    if request.method =="POST":
        formulario=AuthenticationForm(request, data= request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            usuario = data.get('username')
            password = data.get('password')
            user = authenticate(username=usuario, password=password)

            if user: #is not None
                login(request=request, user=user)
                if next_url:
                    return redirect(next_url)
                return redirect(reverse('lista_articulos'))
    else:
        formulario=AuthenticationForm()
    return render(
        request=request,
        template_name='perfiles/login.html',
        context={'form':formulario},
    )


class CustomLogoutView(LogoutView):
    template_name= 'perfiles/logout.html'
    
