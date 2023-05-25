from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
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
    
    