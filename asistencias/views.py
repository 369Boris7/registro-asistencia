from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Asistencia
from .serializers import AsistenciaSerializer


class AsistenciaViewSet(viewsets.ModelViewSet):
    queryset = Asistencia.objects.all().order_by("-id")
    serializer_class = AsistenciaSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        curso = self.request.query_params.get("curso")

        if curso:
            queryset = queryset.filter(curso__icontains=curso)

        return queryset


@api_view(["GET"])
def health(request):
    return Response({"status": "ok"})


@api_view(["GET"])
def version(request):
    return Response(
        {
            "application": "registro-asistencia",
            "version": "1.0.1",
        }
    )
