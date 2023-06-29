from django.contrib import admin

from .models import PreguntaUno, PreguntaDos, PreguntaTres, PreguntaCinco


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
    list_display = ['texto_respuesta']