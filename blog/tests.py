from django.test import TestCase
from django.urls import reverse
from blog.models import Articulo


# Create your tests here.
class ArticuloModelTest(TestCase):
    def test_crear_articulo(self):
        articulo = Articulo.objects.create(titulo='Mi artículo de prueba', cuerpo='Contenido del artículo')
        self.assertEqual(articulo.titulo, 'Mi artículo de prueba')
        self.assertEqual(articulo.cuerpo, 'Contenido del artículo')
