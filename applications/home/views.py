from django.views.generic import TemplateView
from django.shortcuts import render

# importar modelos
from . models import Countdown, PreguntasFrecuentes, Documentos, TipoDocumentos, SeccionDocumentos

# importar apps de terceros


class HomePageView(TemplateView):
    template_name = 'apps/home/home.html'


class ProcesoParticipativoView(TemplateView):
    template_name = 'apps/home/proceso_participativo.html'


class PreguntasFrecuentesView(TemplateView):
    template_name = 'apps/home/preguntas_frecuentes.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['preguntas'] = PreguntasFrecuentes.objects.all()

        return context


class DocumentosView(TemplateView):
    template_name = 'apps/home/documentos.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tipos_documentos = TipoDocumentos.objects.select_related('secciondocumentos_set__documentos').all()
        context['tipos_documentos'] = tipos_documentos
        return context

class PoliticasPrivacidadView(TemplateView):
    template_name = 'apps/home/politicas_privacidad.html'

class OnboardingView(TemplateView):
    template_name = 'apps/home/onboarding.html'

class CountdownView(TemplateView):
    template_name = 'components/countdown.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        countdown = Countdown.objects.first()
        context['end_date'] = countdown.end_date.strftime("%d/%m/%Y")
        context['days_left'] = countdown.get_days_left()
        context['total_days'] = countdown.get_total_days()

        # Calcula el porcentaje de días restantes
        if context['total_days'] != 0:  # Evita la división por cero
            context['progress_percentage'] = (context['days_left'] / context['total_days']) * 100
        else:
            context['progress_percentage'] = 0  # Si total_days es 0, entonces el progreso es 0

        return context


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
    