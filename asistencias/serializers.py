from rest_framework import serializers

from .models import Asistencia


class AsistenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asistencia
        fields = (
    "id",
    "nombre_estudiante",
    "curso",
    "fecha",
    "presente",
)
