from django.views.generic import TemplateView, ListView
from django.shortcuts import render
from applications.noticiasymedia.views import NoticiasView, MultimediaView
# importar modelos
from .models import Countdown, PreguntasFrecuentes, Documentos, TipoDocumentos, SeccionDocumentos, ConsejoAsesor


from django.http import HttpResponse
from datetime import datetime
from django.contrib.auth.decorators import user_passes_test
from django.contrib.admin.views.decorators import staff_member_required
import csv
from applications.regioncomuna.models import Comuna
from applications.surveys.models import (
    PreguntaUno, PreguntaDos, PreguntaTres,
    PreguntaCinco, PreguntaSeis, PreguntaSiete
)
from applications.users.models import User


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
    
def superuser_required(view_func):
    decorated_view_func = user_passes_test(
        lambda u: u.is_superuser,
        login_url='/admin/login/'
    )(view_func)
    return decorated_view_func

@superuser_required
def generar_reporte_completo(request):
    # Obtener la fecha actual y formatearla
    fecha_actual = datetime.now().strftime('%Y-%m-%d')
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = f'attachment; filename="reporte_completo_{fecha_actual}.csv"'

    writer = csv.writer(response)
    writer.writerow([
        'region', 'comuna', 'genero', 'edad', 'pueblo_originario', 'fecha_encuesta_completada',
        PreguntaUno._meta.get_field('valor').verbose_name,
        PreguntaDos._meta.get_field('propuesta_1').verbose_name,
        PreguntaDos._meta.get_field('propuesta_2').verbose_name,
        PreguntaDos._meta.get_field('propuesta_3').verbose_name,
        PreguntaDos._meta.get_field('propuesta_4').verbose_name,
        PreguntaTres._meta.get_field('iniciativa_1').verbose_name,
        PreguntaTres._meta.get_field('iniciativa_2').verbose_name,
        PreguntaTres._meta.get_field('iniciativa_3').verbose_name,
        PreguntaTres._meta.get_field('iniciativa_4').verbose_name,
        PreguntaTres._meta.get_field('iniciativa_5').verbose_name,
        PreguntaCinco._meta.verbose_name,
        PreguntaSeis._meta.get_field('valor').verbose_name,
        PreguntaSiete._meta.get_field('texto_respuesta').verbose_name
    ])

    usuarios = User.objects.all()
    for usuario in usuarios:
        row = [
            usuario.comuna.region.region if usuario.comuna and usuario.comuna.region else '',
            usuario.comuna.comuna if usuario.comuna else '',
            usuario.get_genero_display(),
            usuario.edad,
            usuario.get_pueblo_originario_display(),
            usuario.fecha_encuesta_completada.strftime('%Y-%m-%d %H:%M:%S') if usuario.fecha_encuesta_completada else '',
        ]
        
        # PreguntaUno
        pregunta_uno = PreguntaUno.objects.filter(usuario=usuario).first()
        row.append(pregunta_uno.get_valor_display() if pregunta_uno else '')

        # PreguntaDos
        pregunta_dos = PreguntaDos.objects.filter(usuario=usuario).first()
        row.extend([
            pregunta_dos.get_propuesta_1_display() if pregunta_dos else '',
            pregunta_dos.get_propuesta_2_display() if pregunta_dos else '',
            pregunta_dos.get_propuesta_3_display() if pregunta_dos else '',
            pregunta_dos.get_propuesta_4_display() if pregunta_dos else ''
        ])
        
        # PreguntaTres
        pregunta_tres = PreguntaTres.objects.filter(usuario=usuario).first()
        row.extend([
            pregunta_tres.get_iniciativa_1_display() if pregunta_tres else '',
            pregunta_tres.get_iniciativa_2_display() if pregunta_tres else '',
            pregunta_tres.get_iniciativa_3_display() if pregunta_tres else '',
            pregunta_tres.get_iniciativa_4_display() if pregunta_tres else '',
            pregunta_tres.get_iniciativa_5_display() if pregunta_tres else ''
        ])
        
        # PreguntaCinco
        pregunta_cinco = PreguntaCinco.objects.filter(usuario=usuario).first()
        row.append(', '.join(pregunta_cinco.get_opciones_texto()) if pregunta_cinco else '')

        # PreguntaSeis
        pregunta_seis = PreguntaSeis.objects.filter(usuario=usuario).first()
        row.append(pregunta_seis.get_valor_display() if pregunta_seis else '')

        # PreguntaSiete
        pregunta_siete = PreguntaSiete.objects.filter(usuario=usuario).first()
        row.append(pregunta_siete.texto_respuesta if pregunta_siete else '')

        writer.writerow(row)

    return response