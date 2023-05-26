from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LogoutView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from perfiles.forms import UserRegisterForm, UserUpdateForm, AvatarForm 
from perfiles.models import Avatar


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



@login_required
def custom_logout_view(request):
    view = LogoutView.as_view(template_name='perfiles/logout.html')
    return view(request)
    


@login_required
def mi_perfil_update(request):
    if request.method == "POST":
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = UserUpdateForm(instance=request.user)

    contexto = {'form': form}
    return render(
        request=request, 
        template_name='perfiles/formulario_perfil.html', 
        context=contexto
    )


@login_required
def agregar_avatar(request):
    try:
        avatar = Avatar.objects.get(user=request.user)
    except Avatar.DoesNotExist:
        avatar = None

    if request.method == "POST":
        form = AvatarForm(request.POST, request.FILES, instance=avatar)
        if form.is_valid():
            avatar= form.save()
            avatar.user= request.user
            avatar.save()
            return redirect('inicio')
    else:
        form= AvatarForm(instance= avatar)

    return render(
        request=request, 
        template_name='perfiles/formulario_avatar.html',
        context= {'form': form},
    )