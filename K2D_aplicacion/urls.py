from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    UsuarioPerfilViewSet, InmuebleViewSet, VisitaViewSet,
    HistorialEstadoInmuebleViewSet, RegistroAuditoriaViewSet
)

# Creamos el router de DRF con los modelos correctos
router = DefaultRouter()
router.register(r'usuarios', UsuarioPerfilViewSet)
router.register(r'inmuebles', InmuebleViewSet)
router.register(r'visitas', VisitaViewSet)
router.register(r'historial-estados', HistorialEstadoInmuebleViewSet)
router.register(r'auditoria', RegistroAuditoriaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]