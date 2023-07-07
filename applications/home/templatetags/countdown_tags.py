from django import template
from applications.home.models import Countdown  # Reemplaza con el camino a tu modelo Countdown

register = template.Library()

@register.inclusion_tag('components/countdown.html')
def countdown_component():
    countdown = Countdown.objects.first()
    return {
        'end_date': countdown.end_date.strftime("%d/%m/%Y"),
        'days_left': countdown.get_days_left(),
    }