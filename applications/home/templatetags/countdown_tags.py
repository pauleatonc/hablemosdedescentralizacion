from django import template
from datetime import datetime
from applications.home.models import Countdown  # Reemplaza con el camino a tu modelo Countdown

register = template.Library()

@register.inclusion_tag('components/countdown.html')
def countdown_component():
    countdown = Countdown.objects.first()
    days_left = countdown.get_days_left()
    total_days = countdown.get_total_days()

    # Calcula los días transcurridos desde la fecha de inicio
    today = datetime.now().date()
    days_since_start = (today - countdown.start_date).days

    # Calcula el porcentaje de días transcurridos
    if total_days != 0:  # Evita la división por cero
        progress_percentage = (days_since_start / float(total_days)) * 100
    else:
        progress_percentage = 0  # Si total_days es 0, entonces el progreso es 0

    return {
        'end_date': countdown.end_date.strftime("%d/%m/%Y"),
        'days_left': days_left,
        'total_days': total_days,
        'progress_percentage': int(progress_percentage),  # Se convierte a entero
    }
