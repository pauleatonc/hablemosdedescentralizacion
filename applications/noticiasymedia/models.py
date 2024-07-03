# standard library
from datetime import timedelta, datetime

from django.core.exceptions import ValidationError
#
from django.db import models
from django.template.defaultfilters import slugify
from django.utils.safestring import mark_safe
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill, ResizeToFit, Transpose
# apps de terceros
from model_utils.models import TimeStampedModel

from applications.regioncomuna.models import Region


class Tag(models.Model):
    tag = models.CharField(
        max_length=20, verbose_name='Tag', unique=True)

    def __str__(self):
        return self.tag


class Noticias(TimeStampedModel):
    titulo_noticia = models.CharField(max_length=150 ,verbose_name='Titulo Noticia (obligatorio)', unique=True)
    bajada_noticia = models.CharField(max_length=150, verbose_name='Bajada noticia(obligatorio)')
    contenido_noticia = models.TextField(verbose_name='contenido Noticia (obligatorio)')
    autor = models.CharField(max_length=100, verbose_name='autor (opcional)', blank=True)
    slug = models.SlugField(editable=False, max_length=300)
    tag = models.ManyToManyField(
        Tag, blank=False, verbose_name='Tag noticia')
    portada_noticia= ProcessedImageField(
        upload_to='noticias', processors=[Transpose(), ResizeToFit(1200, 630)],
        format='WEBP',
        options={'quality': 60},
        null=True,
        blank=False,
        verbose_name='Foto Portada (obligatorio)'
    )
    galeria_url = models.URLField(max_length=200, null=True,
                            blank=True, verbose_name='Url galeria de fotos')
    public = models.BooleanField(default=True, verbose_name='publico')

    def __str__(self):
        return self.titulo_noticia

    def save(self, *args, **kwargs):
        now = datetime.now()
        total_time = timedelta(
            hours=now.hour,
            minutes=now.minute,
            seconds=now.second
        )
        seconds = int(total_time.total_seconds())
        slug_unique = '%s %s' % (self.titulo_noticia, str(seconds))

        self.slug = slugify(slug_unique)

        super(Noticias, self).save(*args, **kwargs)
    
    
class Multimedia(TimeStampedModel):
    titulo_multimedia = models.CharField(max_length=200,verbose_name='Titulo Multimedia (obligatorio)', unique=True)
    descripcion_multimedia = models.TextField(verbose_name='Descripcion')
    autor = models.CharField(max_length=100, verbose_name='autor (opcional)', blank=True)
    video_url = models.URLField(max_length=200, null=True,
                            verbose_name='Url video Youtube (obligatorio)')
    tag = models.ManyToManyField(
            Tag, blank=False, verbose_name='Tag Multimedia')
    slug = models.SlugField(editable=False, max_length=300, default='video') 
    public = models.BooleanField(default=True, verbose_name='publico')

    def __str__(self):
        return self.titulo_multimedia
    def save(self, *args, **kwargs):
        now = datetime.now()
        total_time = timedelta(
            hours=now.hour,
            minutes=now.minute,
            seconds=now.second
        )    
        seconds = int(total_time.total_seconds())
        slug_unique = '%s %s' % (self.titulo_multimedia, str(seconds))
        
        self.slug = slugify(slug_unique)
        
        super(Multimedia, self).save(*args,**kwargs)


class PhotoAlbum(TimeStampedModel):
    titulo_album = models.CharField(max_length=200, verbose_name='Titulo Album', null=True, blank=True)
    descripcion_album = models.CharField(max_length=500, verbose_name='Descripcion Album (obligatorio)')
    region = models.ForeignKey(Region, on_delete=models.CASCADE, verbose_name='Region (obligatorio)')
    date = models.DateField(verbose_name='Fecha del Álbum (obligatorio)')
    foto_portada = ProcessedImageField(upload_to='album_photos', processors=[
        ResizeToFill(1200, 630)], format='WEBP', options={'quality': 60}, null=True,
        blank=False, verbose_name='Foto Portada (obligatorio)')
    autor = models.ForeignKey(
        'users.User', on_delete=models.CASCADE, verbose_name='Autor')
    public = models.BooleanField(default=True, verbose_name='Público')

    def __str__(self):
        return self.titulo_album if self.titulo_album else "Álbum sin título"

    class Meta:
        ordering = ['region__region']
        unique_together = ('region', 'date')


class Photo(TimeStampedModel):
    album = models.ForeignKey(
        PhotoAlbum, on_delete=models.CASCADE, verbose_name='Album')
    foto = ProcessedImageField(
        upload_to='album',
        processors=[Transpose(), ResizeToFit(1200, 630)],
        format='WEBP',
        options={'quality': 60},
        null=True,
        blank=False,
        verbose_name='Foto (obligatorio)'
    )
    descripcion = models.CharField(
        max_length=500, verbose_name='Descripcion Foto (obligatorio)')

    def __str__(self):
        return self.descripcion

    def clean(self):
        # Comprobar si el álbum ya tiene 12 fotos
        if Photo.objects.filter(album=self.album).count() >= 12:
            raise ValidationError(f"El álbum '{self.album.titulo_album}' no puede tener más de 12 fotos.")

    def save(self, *args, **kwargs):
        self.clean()  # Llama a clean para realizar la validación antes de guardar
        super().save(*args, **kwargs)

    def preview(self):
        if self.foto:
            return mark_safe(f'<img src="{self.foto.url}" width="150" height="150" />')
        return "No Image"

    preview.short_description = 'Preview'