from django.contrib import admin
from django.urls import path
from perfiles.views import registro, login_view, custom_logout_view, mi_perfil_update

urlpatterns = [
    path('registro/', registro, name="registro"),
    path('login/', login_view, name="login"),
    path('logout/', custom_logout_view, name="logout"),
    path('editar-mi-perfil/', mi_perfil_update, name="editar-perfil"),
]
