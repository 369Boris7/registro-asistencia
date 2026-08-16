from django.http import JsonResponse
from rest_framework.decorators import api_view

from .models import Asistencia
from .serializers import AsistenciaSerializer


@api_view(["GET"])
def health(request):
    return JsonResponse({"status": "ok"}, status=200)


@api_view(["GET"])
def version(request):
    return JsonResponse({"version": "1.0.0"}, status=200)


@api_view(["GET", "POST"])
def registrar_asistencia(request):
    if request.method == "GET":
        asistencias = Asistencia.objects.all()
        serializer = AsistenciaSerializer(
            asistencias,
            many=True,
        )

        return JsonResponse(
            serializer.data,
            safe=False,
            status=200,
        )

    serializer = AsistenciaSerializer(data=request.data)

    if not serializer.is_valid():
        return JsonResponse(
            {
                "detail": "Datos incompletos",
                "errors": serializer.errors,
            },
            status=400,
        )

    asistencia = serializer.save()

    return JsonResponse(
        AsistenciaSerializer(asistencia).data,
        status=201,
    )


@api_view(["GET", "PATCH", "DELETE"])
def consultar_asistencia(request, pk):
    try:
        asistencia = Asistencia.objects.get(pk=pk)
    except Asistencia.DoesNotExist:
        return JsonResponse(
            {"detail": "Asistencia no encontrada"},
            status=404,
        )

    if request.method == "GET":
        serializer = AsistenciaSerializer(asistencia)

        return JsonResponse(
            serializer.data,
            status=200,
        )

    if request.method == "DELETE":
        asistencia.delete()

        return JsonResponse(
            {},
            status=204,
        )

    serializer = AsistenciaSerializer(
        asistencia,
        data=request.data,
        partial=True,
    )

    if not serializer.is_valid():
        return JsonResponse(
            {
                "detail": "Datos incorrectos",
                "errors": serializer.errors,
            },
            status=400,
        )

    asistencia = serializer.save()

    return JsonResponse(
        AsistenciaSerializer(asistencia).data,
        status=200,
    )