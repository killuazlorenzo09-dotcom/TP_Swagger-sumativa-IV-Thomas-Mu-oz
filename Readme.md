# Trabajo Práctico: Documentación de API RESTful con Swagger

Este proyecto implementa una API de gestión de Tareas utilizando Django REST Framework, documentada automáticamente con `drf-yasg`.

## 🚀 Instrucciones de Instalación

1.  Clonar el repositorio.
2.  Crear y activar un entorno virtual.
3.  Instalar dependencias:
    ```bash
    pip install django djangorestframework drf-yasg
    ```
4.  Realizar migraciones:
    ```bash
    python manage.py migrate
    ```
5.  Ejecutar el servidor:
    ```bash
    python manage.py runserver
    ```

## 📖 Acceso a la Documentación

Una vez iniciado el servidor, la documentación interactiva está disponible en:
* **Swagger UI:** [http://127.0.0.1:8000/swagger/](http://127.0.0.1:8000/swagger/)

## 📸 Evidencia de Funcionamiento

### 1. Vista General de los Endpoints
A continuación se muestran todos los endpoints documentados disponibles en la API:

![Vista General de Swagger](docs/swagger_general.png)

### 2. Prueba Interactiva (POST /tareas/)
Demostración de la creación exitosa de una tarea utilizando la interfaz de Swagger (Código 201 Created):

![Prueba de Petición POST](docs/swagger_request.png)

## 🛠 Tecnologías Usadas
* Python
* Django
* Django REST Framework
* drf-yasg (Swagger/OpenAPI)