from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .functions import validar_rut
from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):

    rut = models.CharField(max_length=15, validators=[validar_rut], unique=True)
    password = models.CharField(max_length=200, blank=True)
    email = models.TextField(max_length=100, blank=True, null=True)

    #preguntas del formulario


    #Setiando el nombre de usuario al rut
    USERNAME_FIELD = 'rut'    

    is_staff = models.BooleanField('Usuario administrador', default=False)
    is_active = models.BooleanField(default=True)

    #Campos requeridos
    REQUIRED_FIELDS = ['email']

    objects = UserManager()

    def save(self, *args, **kwargs):
        # Formatear el RUT antes de guardar
        rut_formateado = validar_rut(self.rut)
        self.rut = rut_formateado
        super().save(*args, **kwargs)