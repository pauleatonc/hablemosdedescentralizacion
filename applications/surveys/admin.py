from django.contrib import admin

from .models import PreguntaUno, PreguntaDos, Respuesta, PreguntaTres, PreguntaCinco


@admin.register(PreguntaUno)
class PreguntaUnoAdmin(admin.ModelAdmin):
    list_display = ['valor']


@admin.register(PreguntaDos)
class PreguntaDosAdmin(admin.ModelAdmin):
    list_display = ['prioridad_1', 'prioridad_2', 'prioridad_3', 'prioridad_4']


@admin.register(PreguntaTres)
class PreguntaTresAdmin(admin.ModelAdmin):
    list_display = ['prioridad_1', 'prioridad_2', 'prioridad_3', 'prioridad_4', 'prioridad_5']

@admin.register(PreguntaCinco)
class PreguntaCincoAdmin(admin.ModelAdmin):
    list_display = ['texto_respuesta']

@admin.register(Respuesta)
class RespuestaAdmin(admin.ModelAdmin):
    list_display = ['usuario', 'pregunta_uno', 'pregunta_dos', 'pregunta_tres', 'pregunta_cinco', 'fecha_envio']