from django import forms
from blog.models import Articulo

class ArticuloForm(forms.ModelForm):
    imagen = forms.ImageField(widget=forms.FileInput())
    class Meta:
        model = Articulo
        fields = ['titulo', 'subtitulo', 'cuerpo', 'imagen']

       