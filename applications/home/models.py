from django.db import models

# apps terceros
from model_utils.models import TimeStampedModel


class Contact(TimeStampedModel):
    """Formulario de contacto"""

    CONTACT_REASON_CHOICES = (
        ('sugerencia', 'Sugerencia'),
        ('consulta', 'Consulta por programa'),
        ('documento', 'Falta un documento'),
        ('falla', 'Falla en la plataforma')
    )

    full_name = models.CharField('Nombre completo (obligatorio)', max_length=60)
    email = models.EmailField('Correo electrónico institucional (obligatorio)')
    contact_reason = models.CharField('Razón de contacto (obligatorio)', max_length=30, choices=CONTACT_REASON_CHOICES)
    message = models.TextField('Comentario (obligatorio)')

    class Meta:
        verbose_name = 'Contacto'
        verbose_name_plural = 'Mensajes'

    def __str__(self):
        return self.full_name
