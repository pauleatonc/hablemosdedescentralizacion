from django.views.generic import TemplateView, ListView
from django.shortcuts import render
from applications.noticiasymedia.views import NoticiasView, MultimediaView
# importar modelos
from .models import Countdown, PreguntasFrecuentes, Documentos, TipoDocumentos, SeccionDocumentos, ConsejoAsesor


# importar apps de terceros


class HomePageView(NoticiasView,MultimediaView):
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
        tipos_documentos = TipoDocumentos.objects.prefetch_related('secciondocumentos_set__seccion_documentos').all()
        context['tipos_documentos'] = tipos_documentos
        return context


class PoliticasPrivacidadView(TemplateView):
    template_name = 'apps/home/politicas_privacidad.html'


class OnboardingView(TemplateView):
    template_name = 'apps/home/onboarding.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        countdown = Countdown.objects.first()
        if countdown is None:
            context['is_active'] = False
        else:
            days_until_start = countdown.get_days_until_start()
            days_left = countdown.get_days_left()
            context['is_active'] = (days_until_start <= 0) and (days_left >= 0)
        return context


class DescentralizacionBienestarView(TemplateView):
    template_name = 'apps/home/descentralizacion_bienestar.html'


class ConsejoAsesorListView(ListView):
    model = ConsejoAsesor
    template_name = 'apps/home/consejo_asesor_list.html'
    context_object_name = 'asesores'

    def get_queryset(self):
        # Ordenar por ID de manera descendente
        return ConsejoAsesor.objects.all().order_by('-id')



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
    