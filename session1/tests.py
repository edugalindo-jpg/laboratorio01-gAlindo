from django.test import TestCase
from django.urls import reverse


class BienvenidoViewTests(TestCase):
    def test_bienvenido_devuelve_200(self):
        response = self.client.get(reverse("session1:bienvenido"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Bienvenido a Laboratorio 01")

    def test_raiz_redirige_a_bienvenido(self):
        response = self.client.get("/")
        self.assertRedirects(response, reverse("session1:bienvenido"))

    def test_admin_no_registrado(self):
        response = self.client.get("/admin/login/?next=/admin/")
        self.assertEqual(response.status_code, 404)
