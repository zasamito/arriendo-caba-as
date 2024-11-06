"""
URL configuration for proyecto_cabañas project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from principal import views  # Asegúrate de que este sea el nombre correcto de tu aplicación

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),  # Ruta para la página de inicio
    path('login/', views.login, name='login'),  # Ruta para la página de inicio de sesión
    path('registro/', views.registro, name='registro'),  # Ruta para la página de registro
    path('reservar/', views.reservar, name='reservar'),  # Ruta para la página de reserva
    path('comentarios/', views.comentarios, name='comentarios'),  # Ruta para la página de comentarios
    path('pagos/', views.pagos, name='pagos'),  # Ruta para la página de pagos
    path('cabañas/', views.cabañas, name='cabañas'),  # Ruta para la página de cabañas
    path('guardar_comentario/', views.guardar_comentario, name='guardar_comentario'),  # Nueva ruta para guardar comentarios
]
