# Create your tests here.
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Consulta, Categoria

class ConsultaTramiteTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Crear una categoría para las consultas
        cls.categoria_tramites = Categoria.objects.create(nombre='Tramites')

        # Crear un usuario que puede editar
        cls.usuario_sjm = User.objects.create_user(username='usuario_sjm', password='pass123')
        # Crear un usuario que no puede editar
        cls.usuario_no_sjm = User.objects.create_user(username='usuario_no_sjm', password='pass123')

        # Crear una consulta
        cls.consulta = Consulta.objects.create(
            titulo='Consulta de Ejemplo',
            descripcion='Descripción de la consulta',
            categoria=cls.categoria_tramites
        )

    def test_consulta_view_access(self):
        # Prueba que un usuario autenticado puede acceder a la vista
        self.client.login(username='usuario_no_sjm', password='pass123')
        response = self.client.get(reverse('tramites'))  # Cambia 'tramites' al nombre de tu vista
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Consulta de Ejemplo')

    def test_no_consultas_notification(self):
        # Prueba que muestra una notificación si no hay consultas
        self.client.login(username='usuario_no_sjm', password='pass123')
        # Eliminar la consulta creada para esta prueba
        self.consulta.delete()
        response = self.client.get(reverse('tramites'))  # Cambia 'tramites' al nombre de tu vista
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'No existen noticias en la categoría.')

    def test_only_sjm_can_edit(self):
        # Prueba que solo usuarios SJM pueden editar o eliminar
        self.client.login(username='usuario_sjm', password='pass123')
        response = self.client.get(reverse('editar_consulta', args=[self.consulta.id]))  # Cambia 'editar_consulta' al nombre de tu vista de edición
        self.assertEqual(response.status_code, 200)

        self.client.logout()

        self.client.login(username='usuario_no_sjm', password='pass123')
        response = self.client.get(reverse('editar_consulta', args=[self.consulta.id]))
        self.assertEqual(response.status_code, 403)  # Esperamos que el acceso sea denegado

    def test_responsive_view(self):
        # Asegúrate de que se puede acceder a la vista en diferentes tamaños de pantalla
        self.client.login(username='usuario_no_sjm', password='pass123')
        response = self.client.get(reverse('tramites'))  # Cambia 'tramites' al nombre de tu vista
        self.assertTemplateUsed(response, 'tu_template.html')  # Cambia 'tu_template.html' al nombre de tu plantilla
