from django.test import TestCase
from django.urls import reverse
from mantenedor_lab.models import Laboratorio


class LaboratorioTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Laboratorio.objects.create(nombre_lab='Laboratorio 111', ciudad='Ciudad 1', pais='País 1')

    def test_datos_iniciales(self):
        laboratorio = Laboratorio.objects.get(id=1)
        self.assertEqual(laboratorio.nombre_lab, 'Laboratorio 111')
        self.assertEqual(laboratorio.ciudad, 'Ciudad 1')
        self.assertEqual(laboratorio.pais, 'País 1')

    def test_vista_index(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')


class LaboratorioTest2(TestCase):
    def test_vista_index(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')


class LaboratorioPaginaTest(TestCase):
    def test_pagina(self):
     
        Laboratorio.objects.create(nombre_lab='Laboratorio 111', ciudad='Ciudad 1', pais='País 1')

        url = reverse('index') 
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

        self.assertContains(response, 'Laboratorio 111')
        self.assertContains(response, 'Ciudad 1')
        self.assertContains(response, 'País 1')

        
        self.assertNotContains(response, 'Contenido no deseado') 
