from django.urls import path
from . import views

urlpatterns = [
    # otras rutas...

    # Ruta para iniciar el proceso de login con Clave Única
    path('claveunica/login/', views.claveunica_login, name='claveunica_login'),

    # Ruta para el callback de Clave Única
    path('claveunica/callback/', views.callback, name='claveunica_callback'),

    # otras rutas...
]
