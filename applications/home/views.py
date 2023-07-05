from django.views.generic import TemplateView

# importar modelos
from . models import Countdown

# importar apps de terceros


class HomePageView(TemplateView):
    template_name = 'apps/home/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        countdown = Countdown.objects.first()  # Obtén la instancia de Countdown que deseas mostrar
        context['end_date'] = countdown.end_date.strftime("%d/%m/%Y")  # Formatea la fecha como "dd/mm/aaaa"
        context['days_left'] = countdown.get_days_left()  # Agrega days_left al contexto
        return context

class ProcesoParticipativoView(TemplateView):
    template_name = 'apps/home/proceso_participativo.html'

class PreguntasFrecuentesView(TemplateView):
    template_name = 'apps/home/preguntas_frecuentes.html'

class DocumentosView(TemplateView):
    template_name = 'apps/home/documentos.html'

class PoliticasPrivacidadView(TemplateView):
    template_name = 'apps/home/politicas_privacidad.html'

class Error404(TemplateView):
    template_name = 'apps/errores/error404.html'
   
class Error500(TemplateView):
    template_name = 'apps/errores/error500.html'

    @classmethod
    def as_error_view(cls):

        v = cls.as_view()
        def view(request):
            r = v(request)
            r.render()
            return r
        return view


class Error503(TemplateView):
    template_name = 'apps/errores/error503.html'

    @classmethod
    def as_error_view(cls):
        v = cls.as_view()

        def view(request):
            r = v(request)
            r.render()
            return r

        return view
    