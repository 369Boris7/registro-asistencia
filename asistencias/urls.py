from django.urls import path

from .views import (
    health,
    version,
    registrar_asistencia,
    consultar_asistencia,
)

urlpatterns = [
    path("health", health, name="health"),
    path("version", version, name="version"),

    path(
        "asistencias/",
        registrar_asistencia,
        name="registrar_asistencia",
    ),
    path(
        "asistencias/<int:pk>/",
        consultar_asistencia,
        name="consultar_asistencia",
    ),
]