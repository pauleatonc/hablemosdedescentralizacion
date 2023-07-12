from django.contrib import admin
from import_export.admin import ImportExportMixin
from import_export.resources import ModelResource

from .models import Countdown, TipoDocumentos, SeccionDocumentos, Documentos, PreguntasFrecuentes

from datetime import datetime


class CountdownAdmin(admin.ModelAdmin):
    list_display = ['start_date', 'end_date', 'get_days_left', 'get_total_days']
    readonly_fields = ['get_days_left', 'get_total_days']

    def get_days_left(self, obj):
        if obj.end_date is None:
            return None
        return obj.get_days_left()

    get_days_left.short_description = 'Días para el cierre del proceso'

    def get_total_days(self, obj):
        if obj.start_date is None or obj.end_date is None:
            return None
        return obj.get_total_days()

    get_total_days.short_description = 'Días totales del proceso'

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
class SeccionDocumentosAdmin(ImportExportMixin, admin.ModelAdmin):
    resource_class = SeccionDocumentosResource
    list_display = ('seccion_documento', 'tipo_documento')  # Mostrar el tipo de documento en la lista
    list_filter = ('tipo_documento',)  # Permitir filtrar por tipo de documento

    
class DocumentosResource(ModelResource):
    class Meta:
        model = Documentos


@admin.register(Documentos)
class RegionAdmin(ImportExportMixin, admin.ModelAdmin):
    resource_class = DocumentosResource
    list_display = ('titulo_documento', 'seccion_documento', 'public')  # Mostrar el tipo de documento en la lista
    list_filter = ('seccion_documento',)  # Permitir filtrar por tipo de documento

    # Definir una acción personalizada para editar el campo 'public'
    def make_public(self, request, queryset):
        queryset.update(public=True)

    def make_private(self, request, queryset):
        queryset.update(public=False)

    # Configurar metadatos para la acción personalizada
    make_public.short_description = "Marcar como público"
    make_private.short_description = "Marcar como privado"

    # Agregar las acciones personalizadas al administrador
    actions = [make_public, make_private]