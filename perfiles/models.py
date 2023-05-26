from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Avatar(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True) #un usuario puede tener un avatar
    imagen = models.ImageField(upload_to='avatares/') #se guarda la ruta, no la imagen

    def __str__(self):
        return f" Avatar de: {self.user}"
    
    def actualizar_imagen(self, nueva_imagen):
        self.imagen = nueva_imagen
        self.save()




