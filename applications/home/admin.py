from django.contrib import admin

from .models import Countdown

from datetime import datetime


class CountdownAdmin(admin.ModelAdmin):
    list_display = ['end_date', 'days_left']
    readonly_fields = ['days_left']

    def days_left(self, obj):
        # Calcula los días restantes
        today = datetime.now().date()
        days_left = (obj.end_date - today).days  # Corrección aquí
        return days_left

    days_left.short_description = 'Días para el cierre del proceso'  # Descripción para la columna en la lista de objetos


admin.site.register(Countdown, CountdownAdmin)