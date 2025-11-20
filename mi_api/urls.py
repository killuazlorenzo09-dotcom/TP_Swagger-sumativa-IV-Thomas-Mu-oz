# mi_api/urls.py

from rest_framework.routers import DefaultRouter
from .views import TareaViewSet

# Crea una instancia del Router
router = DefaultRouter()

# Registra el ViewSet. Las rutas serán /api/tareas/
router.register(r'tareas', TareaViewSet)

# Las urlpatterns de la app serán todas las rutas generadas por el router
urlpatterns = router.urls