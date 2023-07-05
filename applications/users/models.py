from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .functions import validar_rut
from .managers import UserManager
from applications.regioncomuna.models import Comuna


class User(AbstractBaseUser, PermissionsMixin):

    USER_GENRE_CHOICES = (
        ('FEM', 'Femenino'),
        ('MASC', 'Masculino'),
        ('NOBIN', 'No binarie'),
        ('PND', 'Prefiero no decirlo')
    )

    rut = models.CharField(max_length=15, validators=[validar_rut], unique=True)
    password = models.CharField(max_length=200, blank=True)
    email = models.TextField(max_length=100, blank=True, null=True)
    genero = models.CharField(max_length=5, choices=USER_GENRE_CHOICES, blank=True, null=True)
    comuna = models.ForeignKey(Comuna, null=True, blank=True, verbose_name='Comuna', on_delete=models.SET_NULL)
    edad = models.PositiveIntegerField(blank=True, null=True)
    politica_privacidad = models.BooleanField(blank=True, null=True, default=False)

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