from django.db import models


class Asistencia(models.Model):
    nombre_estudiante = models.CharField(max_length=100)
    curso = models.CharField(max_length=100)
    fecha = models.DateField()
    presente = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nombre_estudiante} - {self.curso}"
