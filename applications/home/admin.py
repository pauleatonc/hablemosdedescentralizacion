from django.contrib import admin
from import_export.admin import ImportExportMixin
from import_export.resources import ModelResource

from .models import Countdown, TipoDocumentos, SeccionDocumentos, Documentos, PreguntasFrecuentes

from datetime import datetime


class CountdownAdmin(admin.ModelAdmin):
    list_display = ['end_date', 'days_left']
    readonly_fields = ['days_left']

    def days_left(self, obj):
        if obj.end_date is None:
            return None  # Opcional: Puedes retornar None o un valor específico cuando end_date es None
        today = datetime.now().date()
        days_left = (obj.end_date - today).days
        return days_left

    days_left.short_description = 'Días para el cierre del proceso'  # Descripción para la columna en la lista de objetos


admin.site.register(Countdown, CountdownAdmin)


class PreguntasFrecuentesResource(ModelResource):
    class Meta:
        model = PreguntasFrecuentes

@admin.register(PreguntasFrecuentes)
class RegionAdmin(ImportExportMixin, admin.ModelAdmin):
    resource_class = PreguntasFrecuentesResource


class TipoDocumentosResource(ModelResource):
    class Meta:
        model = TipoDocumentos


@admin.register(TipoDocumentos)
class RegionAdmin(ImportExportMixin, admin.ModelAdmin):
    resource_class = TipoDocumentosResource
    
    
class SeccionDocumentosResource(ModelResource):
    class Meta:
        model = SeccionDocumentos


@admin.register(SeccionDocumentos)
class RegionAdmin(ImportExportMixin, admin.ModelAdmin):
    resource_class = SeccionDocumentosResource
    
    
class DocumentosResource(ModelResource):
    class Meta:
        model = Documentos


@admin.register(Documentos)
class RegionAdmin(ImportExportMixin, admin.ModelAdmin):
    resource_class = DocumentosResource