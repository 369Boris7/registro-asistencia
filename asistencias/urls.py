from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import AsistenciaViewSet, health, version

router = DefaultRouter()
router.register("asistencias", AsistenciaViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("health", health),
    path("version", version),
]
