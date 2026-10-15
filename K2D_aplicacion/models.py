from django.db import models
from django.utils import timezone

# 1. Modelo de Perfil de Usuario (Extensión del usuario del sistema)
class UsuarioPerfil(models.Model):
    # Tipos de usuarios definidos en el requerimiento
    TIPO_USUARIO_CHOICES = [
        ('PERSONA', 'Persona Natural Propietaria'),
        ('INMOBILIARIA', 'Empresa Inmobiliaria'),
        ('AGENTE', 'Agente / Corredor'),
        ('CLIENTE', 'Cliente / Interesado'),
    ]

    rut_tax_id = models.CharField(max_length=15, unique=True, null=False)
    tipo_usuario = models.CharField(max_length=20, choices=TIPO_USUARIO_CHOICES, null=False)
    nombre_o_razon_social = models.CharField(max_length=100, null=False)
    email = models.EmailField(unique=True, null=False)
    telefono = models.CharField(max_length=15, null=False)
    direccion = models.TextField(max_length=200, null=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.nombre_o_razon_social} ({self.tipo_usuario})"


# 2. Modelo para los Inmuebles / Propiedades
class Inmueble(models.Model):
    TIPO_PROPIEDAD_CHOICES = [
        ('CASA', 'Casa'),
        ('DEPARTAMENTO', 'Departamento'),
        ('OFICINA', 'Oficina'),
        ('TERRENO', 'Terreno'),
    ]

    TIPO_OPERACION_CHOICES = [
        ('VENTA', 'Venta'),
        ('ARRIENDO', 'Arriendo'),
    ]

    ESTADO_CHOICES = [
        ('DISPONIBLE', 'Disponible'),
        ('RESERVADO', 'Reservado'),
        ('VENDIDO', 'Vendido'),
        ('ARRENDADO', 'Arrendado'),
        ('INACTIVO', 'Inactivo'),
    ]

    # Relación ForeignKey con la persona o empresa dueña de la propiedad
    propietario = models.ForeignKey(UsuarioPerfil, on_delete=models.CASCADE, related_name='propiedades')
    
    titulo = models.CharField(max_length=100, null=False)
    descripcion = models.TextField(max_length=500, null=False)
    tipo_propiedad = models.CharField(max_length=20, choices=TIPO_PROPIEDAD_CHOICES, null=False)
    tipo_operacion = models.CharField(max_length=10, choices=TIPO_OPERACION_CHOICES, null=False)
    precio = models.DecimalField(max_digits=12, decimal_places=2, null=False)
    
    direccion = models.CharField(max_length=150, null=False)
    comuna = models.CharField(max_length=50, null=False)
    region = models.CharField(max_length=50, null=False)
    
    habitaciones = models.IntegerField(default=0)
    banos = models.IntegerField(default=0)
    metros_cuadrados = models.FloatField(null=False)
    
    estado_actual = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='DISPONIBLE')
    es_publica = models.BooleanField(default=True)
    
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.titulo} - {self.comuna} (${self.precio})"


# 3. Modelo para la Gestión de Visitas
class Visita(models.Model):
    ESTADO_VISITA_CHOICES = [
        ('PROGRAMADA', 'Programada'),
        ('REALIZADA', 'Realizada'),
        ('CANCELADA', 'Cancelada'),
        ('REPROGRAMADA', 'Reprogramada'),
    ]

    inmueble = models.ForeignKey(Inmueble, on_delete=models.CASCADE, related_name='visitas')
    cliente = models.ForeignKey(UsuarioPerfil, on_delete=models.CASCADE, related_name='visitas_solicitadas')
    agente = models.ForeignKey(UsuarioPerfil, on_delete=models.SET_NULL, null=True, related_name='visitas_asignadas')
    
    fecha_programada = models.DateField(null=False)
    hora_programada = models.TimeField(null=False)
    estado_visita = models.CharField(max_length=20, choices=ESTADO_VISITA_CHOICES, default='PROGRAMADA')
    comentarios_observaciones = models.TextField(max_length=300, null=True, blank=True)
    
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Visita a {self.inmueble.titulo} - {self.fecha_programada} {self.hora_programada}"


# 4. Modelo para el Historial de Cambios de Estado (Trazabilidad)
class HistorialEstadoInmueble(models.Model):
    inmueble = models.ForeignKey(Inmueble, on_delete=models.CASCADE, related_name='historial_estados')
    usuario = models.ForeignKey(UsuarioPerfil, on_delete=models.SET_NULL, null=True)
    
    estado_anterior = models.CharField(max_length=20, null=False)
    estado_nuevo = models.CharField(max_length=20, null=False)
    motivo_observacion = models.TextField(max_length=200, null=False)
    fecha_cambio = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Cambio estado {self.inmueble.titulo}: {self.estado_anterior} -> {self.estado_nuevo}"


# 5. Modelo para Auditoría de Operaciones
class RegistroAuditoria(models.Model):
    usuario = models.ForeignKey(UsuarioPerfil, on_delete=models.SET_NULL, null=True)
    accion = models.CharField(max_length=100, null=False)
    detalles = models.TextField(max_length=300, null=False)
    fecha_registro = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Auditoría: {self.accion} - {self.fecha_registro}"