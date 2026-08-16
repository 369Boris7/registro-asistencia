from django.contrib import admin
from django.http import JsonResponse
from django.urls import include, path


def inicio(request):
    return JsonResponse(
        {
            "proyecto": "Registro de asistencia",
            "estado": "funcionando",
            "health": "/api/health",
            "version": "/api/version",
            "crud": "/api/asistencias/",
        }
    )


urlpatterns = [
    path("", inicio),
    path("admin/", admin.site.urls),
    path("api/", include("asistencias.urls")),
]
