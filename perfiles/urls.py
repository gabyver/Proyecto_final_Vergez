from django.contrib import admin
from django.urls import path
from perfiles.views import registro, login_view, custom_logout_view, editar_usuario, agregar_avatar

urlpatterns = [
    path('signup/', registro, name="registro"),
    path('login/', login_view, name="login"),
    path('logout/', custom_logout_view, name="logout"),
    path('profile/', editar_usuario, name="editar_perfil"),
    path('agregar-avatar/', agregar_avatar, name="agregar_avatar"),
]
