from django.contrib import admin

from .models import PreguntaUno, PreguntaDos, PreguntaTres, PreguntaCinco, PreguntaSeis, PreguntaSiete, \
    OpcionesPreguntaCinco


@admin.register(PreguntaUno)
class PreguntaUnoAdmin(admin.ModelAdmin):
    list_display = ['valor']


@admin.register(PreguntaDos)
class PreguntaDosAdmin(admin.ModelAdmin):
    list_display = ['propuesta_1', 'propuesta_2', 'propuesta_3', 'propuesta_4']


@admin.register(PreguntaTres)
class PreguntaTresAdmin(admin.ModelAdmin):
    list_display = ['iniciativa_1', 'iniciativa_2', 'iniciativa_3', 'iniciativa_4', 'iniciativa_5']


@admin.register(PreguntaCinco)
class PreguntaCincoAdmin(admin.ModelAdmin):
    list_display = ['usuario', 'get_opciones']

    def get_opciones(self, obj):
        return ", ".join([opcion.texto for opcion in obj.opciones.all()])

    get_opciones.short_description = 'Opciones Seleccionadas'


@admin.register(PreguntaSeis)
class PreguntaSeisAdmin(admin.ModelAdmin):
    list_display = ['valor']


@admin.register(PreguntaSiete)
class PreguntaCSieteAdmin(admin.ModelAdmin):
    list_display = ['texto_respuesta']


@admin.register(OpcionesPreguntaCinco)
class OpcionesPreguntaCincoAdmin(admin.ModelAdmin):
    list_display = ['clave', 'texto']
