# mi_api/models.py

from django.db import models

class Tarea(models.Model):
    """Modelo de Tarea para la demostración de la API."""
    titulo = models.CharField(max_length=200, verbose_name="Título")
    descripcion = models.TextField(blank=True, verbose_name="Descripción")
    completada = models.BooleanField(default=False, verbose_name="Completada")
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
