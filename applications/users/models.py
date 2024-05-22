from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .functions import validar_rut
from .managers import UserManager
from applications.regioncomuna.models import Comuna


class User(AbstractBaseUser, PermissionsMixin):

    USER_GENRE_CHOICES = (
        ('', 'Elige una opción'),
        ('FEM', 'Femenino'),
        ('MASC', 'Masculino'),
        ('NOBIN', 'No binario'),
        ('OTRO', 'Otro'),
        ('PND', 'Prefiero no decirlo')
    )

    USER_PUEBLOS_CHOICES = (
        ('', 'Elige una opción'),
        ('NP', 'No pertenece'),
        ('AIM', 'Aimara'),
        ('ATAC', 'Atacameño'),
        ('COLL', 'Colla'),
        ('CHAN', 'Chango'),
        ('DIAG', 'Diaguita'),
        ('KAW', 'Kawésqar'),
        ('MAPU', 'Mapuche'),
        ('QUEC', 'Quechua'),
        ('RAPA', 'Rapa-Nui'),
        ('SELK', 'Selknam'),
        ('YAG', 'Yagán'),
        ('OTRO', 'Otro'),
    )

    USER_AGE_CHOICES = (
        ('', 'Elige una opción'),
        ('14-18', 'De 14 a 18 años'),
        ('19-25', 'De 19 a 25 años'),
        ('26-35', 'De 26 a 35 años'),
        ('36-45', 'De 36 a 45 años'),
        ('46-55', 'De 46 a 55 años'),
        ('56-65', 'De 56 a 65 años'),
        ('66-75', 'De 66 a 75 años'),
        ('75-120', '76 años o más'),
    )

    FAMILIARIDAD_CHOICES = (
        ("si", "Si"),
        ("no", "No")
    )

    rut = models.CharField(max_length=15, validators=[validar_rut], unique=True)
    password = models.CharField(max_length=200, blank=True)
    email = models.TextField(max_length=100, blank=True, null=True)
    genero = models.CharField(max_length=5, choices=USER_GENRE_CHOICES, blank=True, null=True)
    comuna = models.ForeignKey(Comuna, null=True, blank=True, verbose_name='Comuna', on_delete=models.SET_NULL)
    edad = models.CharField(choices=USER_AGE_CHOICES, blank=True, null=True)
    politica_privacidad = models.BooleanField(blank=True, null=True, default=False)
    encuesta_completada = models.BooleanField(default=False)
    recibir_resultados = models.BooleanField(default=False)
    pueblo_originario = models.CharField(max_length=5, choices=USER_PUEBLOS_CHOICES, blank=True, null=True)
    familiaridad = models.CharField(choices=FAMILIARIDAD_CHOICES, blank=True, null=True)

    #Setiando el nombre de usuario al rut
    USERNAME_FIELD = 'rut'    

    is_staff = models.BooleanField('Usuario administrador', default=False)
    is_active = models.BooleanField(default=True)

    #Campos requeridos
    REQUIRED_FIELDS = ['email']

    objects = UserManager()

#    def save(self, *args, **kwargs):
#        # Formatear el RUT antes de guardar
#        rut_formateado = self.rut
#        self.rut = rut_formateado
#        super().save(*args, **kwargs)
