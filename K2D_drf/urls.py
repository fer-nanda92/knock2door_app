"""
URL configuration for K2D_drf project.
"""
from django.contrib import admin
from django.urls import path, include
from K2D_aplicacion import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Ruta para la página de bienvenida en la raíz
    path('', views.bienvenida, name='bienvenida'),
    
    # Enrutador general para la API de la aplicación
    path('api/', include('K2D_aplicacion.urls')),
]


