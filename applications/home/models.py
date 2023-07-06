from django.db import models
from datetime import datetime

from django.core.validators import FileExtensionValidator
from .functions import validate_file_size_five


class Countdown(models.Model):
    end_date = models.DateField()

    def get_days_left(self):
        today = datetime.now().date()
        days_left = (self.end_date - today).days
        return days_left


class PreguntasFrecuentes(models.Model):

    pregunta_frecuente = models.CharField(max_length=400)
    respuesta_pregunta_frecuente = models.TextField()

    class Meta:
        verbose_name = 'Pregunta frecuente'
        verbose_name_plural = 'Pregunta frecuentes'

    def __str__(self):
        return self.pregunta_frecuente


class TipoDocumentos(models.Model):

    tipo_documento = models.CharField(max_length=50,  unique=True)

    class Meta:
        verbose_name = 'Tipo de documento'
        verbose_name_plural = 'Tipos de documento'

    def __str__(self):
        return self.tipo_documento


class SeccionDocumentos(models.Model):

    seccion_documento = models.CharField(max_length=100, unique=True)
    tipo_documento = models.ForeignKey(TipoDocumentos, blank=False, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'seccion de tipo de documento'
        verbose_name_plural = 'Secciones de tipo de documento'

    def __str__(self):
        return self.seccion_documento


class Documentos(models.Model):

    titulo_documento = models.CharField(max_length=100)
    public = models.BooleanField(default=True)
    seccion_documento = models.ForeignKey(SeccionDocumentos, blank=False, on_delete=models.CASCADE,
                                       related_name='seccion_documentos')
    documento = models.FileField(upload_to='documents',
                             validators=[
                                 FileExtensionValidator(
                                    ['pdf'], message='Solo se permiten archivos PDF.'), validate_file_size_five],
                                 null=True, blank=True)


    class Meta:
        verbose_name = 'Documento'
        verbose_name_plural = 'Documentos'

    def __str__(self):
        return self.titulo_documento