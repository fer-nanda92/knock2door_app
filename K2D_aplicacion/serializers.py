from rest_framework import serializers
from .models import UsuarioPerfil, Inmueble, Visita, HistorialEstadoInmueble, RegistroAuditoria

class UsuarioPerfilSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsuarioPerfil
        fields = '__all__'

class InmuebleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inmueble
        fields = '__all__'

class VisitaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visita
        fields = '__all__'

class HistorialEstadoInmuebleSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistorialEstadoInmueble
        fields = '__all__'

class RegistroAuditoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegistroAuditoria
        fields = '__all__'