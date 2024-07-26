from django import template
from datetime import datetime
from applications.home.models import Countdown  # Reemplaza con el camino a tu modelo Countdown

register = template.Library()

@register.inclusion_tag('components/countdown.html', takes_context=True)
def countdown_component(context):
    countdown = Countdown.objects.first()
    if countdown is None:
        return {
            'end_date': 'No disponible',
            'days_left': 0,
            'days_until_start': 0,
            'total_days': 0,
            'progress_percentage': 0,
        }

    days_left = countdown.get_days_left()
    days_until_start = countdown.get_days_until_start()
    total_days = countdown.get_total_days()

    today = datetime.now().date()
    days_since_start = (today - countdown.start_date).days

    # Calcula el porcentaje de días transcurridos
    if total_days != 0 and days_left is not None:  # Evita la división por cero y cuando aún no ha iniciado
        progress_percentage = (days_since_start / float(total_days)) * 100
    else:
        progress_percentage = 0

    return {
        'end_date': countdown.end_date.strftime("%d/%m/%Y"),
        'days_left': days_left,
        'days_until_start': days_until_start,
        'total_days': total_days,
        'progress_percentage': int(progress_percentage),  # Se convierte a entero
    }