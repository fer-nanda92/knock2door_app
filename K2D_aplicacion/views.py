from django.shortcuts import render  # Asegúrate de importar render
from rest_framework import viewsets
from .models import UsuarioPerfil, Inmueble, Visita, HistorialEstadoInmueble, RegistroAuditoria
from .serializers import (
    UsuarioPerfilSerializer, InmuebleSerializer, VisitaSerializer,
    HistorialEstadoInmuebleSerializer, RegistroAuditoriaSerializer
)

# Vista de bienvenida renderizando el HTML
def bienvenida(request):
    return render(request, 'Bienvenida.html')

# ViewSets para la API REST...
class UsuarioPerfilViewSet(viewsets.ModelViewSet):
    queryset = UsuarioPerfil.objects.all()
    serializer_class = UsuarioPerfilSerializer

class InmuebleViewSet(viewsets.ModelViewSet):
    queryset = Inmueble.objects.all()
    serializer_class = InmuebleSerializer

class VisitaViewSet(viewsets.ModelViewSet):
    queryset = Visita.objects.all()
    serializer_class = VisitaSerializer

class HistorialEstadoInmuebleViewSet(viewsets.ModelViewSet):
    queryset = HistorialEstadoInmueble.objects.all()
    serializer_class = HistorialEstadoInmuebleSerializer

class RegistroAuditoriaViewSet(viewsets.ModelViewSet):
    queryset = RegistroAuditoria.objects.all()
    serializer_class = RegistroAuditoriaSerializergit add .
