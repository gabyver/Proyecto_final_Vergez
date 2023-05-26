from django.db import models
from django.contrib.auth.models import User


class Articulo(models.Model):
    titulo= models.CharField(max_length=200, unique=True)
    subtitulo= models.CharField(max_length=200)
    cuerpo= models.TextField()
    autor= models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    fecha_publicacion= models.DateTimeField(auto_now_add=True)
    imagen= models.ImageField(upload_to='images')

    class Meta:
        ordering = ['-fecha_publicacion']

    def __str__(self):
        return f"{self.titulo} - {self.subtitulo}"
# Create your models here.
