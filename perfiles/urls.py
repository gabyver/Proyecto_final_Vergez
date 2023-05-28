from django.contrib import admin
from django.urls import path
from perfiles.views import registro, login_view, custom_logout_view, mi_perfil_update, agregar_avatar

urlpatterns = [
    path('signup/', registro, name="registro"),
    path('login/', login_view, name="login"),
    path('logout/', custom_logout_view, name="logout"),
    path('profile/', mi_perfil_update, name="editar_perfil"),
    path('agregar-avatar/', agregar_avatar, name="agregar_avatar"),
]
