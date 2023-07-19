# standard library
from datetime import timedelta, datetime
#
from django.db import models
from django.template.defaultfilters import slugify
# apps de terceros
from model_utils.models import TimeStampedModel
from imagekit.models import ImageSpecField
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill


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
    portada_noticia= ProcessedImageField(upload_to='noticias', processors=[
        ResizeToFill(1200, 630)], format='WEBP', options={'quality': 60}, null=True,
        blank=False, verbose_name='Foto Portada (obligatorio)')
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
            Tag, blank=False, verbose_name='Tag noticia')

    public = models.BooleanField(default=True, verbose_name='publico')

    def __str__(self):
        return self.titulo_multimedia
    
