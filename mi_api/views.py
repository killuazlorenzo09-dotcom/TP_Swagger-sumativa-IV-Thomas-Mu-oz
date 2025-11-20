from django.shortcuts import render

# Create your views here.
# mi_api/views.py

from rest_framework import viewsets
from .models import Tarea
from .serializers import TareaSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

class TareaViewSet(viewsets.ModelViewSet):
    """
    ViewSet que proporciona las operaciones CRUD para el modelo Tarea.
    Permite listar, crear, recuperar, actualizar y eliminar tareas pendientes.
    """
    queryset = Tarea.objects.all()
    serializer_class = TareaSerializer

    # Ejemplo de documentación detallada para el método LISTAR (GET /tareas/)
    @swagger_auto_schema(
        operation_description="Obtiene el listado completo de todas las tareas existentes.",
        responses={
            200: TareaSerializer(many=True), # Respuesta de éxito con la lista de tareas
            401: 'No autorizado'
        }
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    # Ejemplo de documentación detallada para el método CREAR (POST /tareas/)
    @swagger_auto_schema(
        operation_description="Crea una nueva tarea. Solo se necesita el título.",
        request_body=TareaSerializer,
        responses={
            201: openapi.Response('Tarea creada exitosamente', TareaSerializer),
            400: 'Datos de entrada inválidos'
        }
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)