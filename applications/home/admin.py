# admin.py dentro de la aplicación home
from django.contrib import admin
from django.utils.safestring import mark_safe
from import_export.admin import ImportExportMixin
from import_export.resources import ModelResource
from django.urls import path
from django.utils.html import format_html
from .views import generar_reporte_completo
from applications.regioncomuna.models import Region, Comuna
from applications.surveys.models import PreguntaUno, PreguntaDos, PreguntaTres, PreguntaCinco, PreguntaSeis, \
    PreguntaSiete, OpcionesPreguntaCinco
from applications.users.models import User

from .models import Countdown, TipoDocumentos, SeccionDocumentos, Documentos, PreguntasFrecuentes, ConsejoAsesor
from ..noticiasymedia.models import PhotoAlbum, Photo


# Definir el CustomAdminSite
class CustomAdminSite(admin.AdminSite):
    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('generar_reporte_completo/', self.admin_view(generar_reporte_completo),
                 name='generar_reporte_completo'),
        ]
        return custom_urls + urls

    def index(self, request, extra_context=None):
        extra_context = extra_context or {}
        extra_context['custom_button'] = format_html('<a class="button" href="{}">Generar Reporte Completo</a>',
                                                     '/admin/generar_reporte_completo/')
        return super().index(request, extra_context=extra_context)


admin_site = CustomAdminSite(name='custom_admin')


# Definir los ModelAdmin
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


class PreguntasFrecuentesResource(ModelResource):
    class Meta:
        model = PreguntasFrecuentes


class PreguntasFrecuentesAdmin(ImportExportMixin, admin.ModelAdmin):
    resource_class = PreguntasFrecuentesResource


class TipoDocumentosResource(ModelResource):
    class Meta:
        model = TipoDocumentos


class TipoDocumentosAdmin(ImportExportMixin, admin.ModelAdmin):
    resource_class = TipoDocumentosResource


class SeccionDocumentosResource(ModelResource):
    class Meta:
        model = SeccionDocumentos


class SeccionDocumentosAdmin(ImportExportMixin, admin.ModelAdmin):
    resource_class = SeccionDocumentosResource
    list_display = ('seccion_documento', 'tipo_documento')
    list_filter = ('tipo_documento',)


class DocumentosResource(ModelResource):
    class Meta:
        model = Documentos


class DocumentosAdmin(ImportExportMixin, admin.ModelAdmin):
    resource_class = DocumentosResource
    list_display = ('titulo_documento', 'seccion_documento', 'public')
    list_filter = ('seccion_documento',)

    def make_public(self, request, queryset):
        queryset.update(public=True)

    def make_private(self, request, queryset):
        queryset.update(public=False)

    make_public.short_description = "Marcar como público"
    make_private.short_description = "Marcar como privado"
    actions = [make_public, make_private]


class ConsejoAsesorAdmin(admin.ModelAdmin):
    list_display = ('nombre_asesor', 'region', 'curriculum', 'avatar_preview')
    list_filter = ('region',)
    search_fields = ('nombre_asesor', 'curriculum')
    readonly_fields = ('avatar_preview',)

    def avatar_preview(self, obj):
        if obj.avatar:
            return mark_safe(f'<img src="{obj.avatar.url}" width="150" height="150" />')
        return "No Image"

    avatar_preview.short_description = 'Avatar'


class PhotoInline(admin.TabularInline):
    model = Photo
    fields = ['foto', 'descripcion']
    extra = 1  # Número de formas extras para cargar por defecto


class PhotoAlbumAdmin(admin.ModelAdmin):
    list_display = ['titulo_album', 'autor', 'region', 'date', 'public']
    inlines = [PhotoInline]

    def save_model(self, request, obj, form, change):
        if not obj.autor_id:  # Asigna el autor solo si es una nueva instancia
            obj.autor = request.user
        super().save_model(request, obj, form, change)


class PhotoAdmin(admin.ModelAdmin):
    list_display = ['album', 'foto', 'descripcion']
    search_fields = ['descripcion', 'album__titulo_album']

    def save_model(self, request, obj, form, change):
        obj.clean()  # Llama a clean para realizar la validación antes de guardar
        super().save_model(request, obj, form, change)


# Registrar los modelos con admin_site en lugar de admin.site
admin_site.register(Countdown, CountdownAdmin)
admin_site.register(PreguntasFrecuentes, PreguntasFrecuentesAdmin)
admin_site.register(TipoDocumentos, TipoDocumentosAdmin)
admin_site.register(SeccionDocumentos, SeccionDocumentosAdmin)
admin_site.register(Documentos, DocumentosAdmin)
admin_site.register(ConsejoAsesor, ConsejoAsesorAdmin)
admin_site.register(Region)
admin_site.register(Comuna)
admin_site.register(PreguntaUno)
admin_site.register(PreguntaDos)
admin_site.register(PreguntaTres)
admin_site.register(PreguntaCinco)
admin_site.register(PreguntaSeis)
admin_site.register(PreguntaSiete)
admin_site.register(OpcionesPreguntaCinco)
admin_site.register(User)
admin_site.register(PhotoAlbum, PhotoAlbumAdmin)
admin_site.register(Photo, PhotoAdmin)
