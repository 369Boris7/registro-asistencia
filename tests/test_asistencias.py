from django.test import TestCase
from rest_framework.test import APIClient

from asistencias.models import Asistencia


class AsistenciaApiTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.registro = Asistencia.objects.create(
            nombre_estudiante="Ana Perez",
            curso="TILE23",
            fecha="2026-08-15",
            presente=True,
        )

    def test_health(self):
        response = self.client.get("/api/health")
        self.assertEqual(response.status_code, 200)

    def test_version(self):
        response = self.client.get("/api/version")
        self.assertEqual(response.status_code, 200)
        self.assertIn("version", response.json())

    def test_listar_asistencias(self):
        response = self.client.get("/api/asistencias/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 1)

    def test_crear_asistencia(self):
        datos = {
            "nombre_estudiante": "Luis Soto",
            "curso": "TILE23",
            "fecha": "2026-08-15",
            "presente": True,
        }

        response = self.client.post(
            "/api/asistencias/",
            datos,
            format="json",
        )

        self.assertEqual(response.status_code, 201)

    def test_consultar_asistencia(self):
        response = self.client.get(f"/api/asistencias/{self.registro.id}/")

        self.assertEqual(response.status_code, 200)

    def test_actualizar_asistencia(self):
        response = self.client.patch(
            f"/api/asistencias/{self.registro.id}/",
            {"presente": False},
            format="json",
        )

        self.assertEqual(response.status_code, 200)
        self.assertFalse(response.json()["presente"])

    def test_eliminar_asistencia(self):
        response = self.client.delete(f"/api/asistencias/{self.registro.id}/")

        self.assertEqual(response.status_code, 204)

    def test_rechazar_datos_incompletos(self):
        response = self.client.post(
            "/api/asistencias/",
            {"nombre_estudiante": "Pedro"},
            format="json",
        )

        self.assertEqual(response.status_code, 400)
