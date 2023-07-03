from django.views.generic import TemplateView, View
from .forms import PreguntaUnoForm, PreguntaDosForm, PreguntaCincoForm, DatosUsuarioForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect
from django.views.generic.edit import FormView
from .models import PreguntaUno, PreguntaDos, PreguntaCinco
from django.contrib.sessions.backends.db import SessionStore
from django.http import JsonResponse
from applications.regioncomuna.models import Region, Comuna
from django.http import JsonResponse

from formtools.wizard.views import SessionWizardView


class ComunasPorRegionView(View):
    def get(self, request, *args, **kwargs):
        region_id = self.kwargs.get('region_id')
        comunas = Comuna.objects.filter(region__id=region_id).values('id', 'comuna')
        comunas_list = list(comunas)
        return JsonResponse(comunas_list, safe=False)


class ConsultaDatosUsuarioView(LoginRequiredMixin, FormView):
    template_name = 'apps/surveys/datos_usuario_form.html'
    form_class = DatosUsuarioForm
    login_url = 'users_app:user-login'  # URL de inicio de sesión

    def form_valid(self, form):
        pregunta = form.save(commit=False)
        pregunta.usuario = self.request.user
        pregunta.save()

        return redirect('surveys_app:pregunta_uno')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['regiones'] = Region.objects.all()
        return context


class PreguntaUnoView(LoginRequiredMixin, FormView):
    template_name = 'apps/surveys/pregunta_uno.html'
    form_class = PreguntaUnoForm
    model = PreguntaUno
    login_url = 'users_app:user-login'  # URL de inicio de sesión

    def form_valid(self, form):
        pregunta_uno = form.save(commit=False)
        pregunta_uno.usuario = self.request.user
        pregunta_uno.save()

        return redirect('surveys_app:pregunta_dos')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        usuario = self.request.user
        try:
            pregunta_uno = PreguntaUno.objects.get(usuario=usuario)
            context['valor_guardado'] = pregunta_uno.get_valor_display()
        except PreguntaUno.DoesNotExist:
            context['valor_guardado'] = None
        return context


class PreguntaDosView(LoginRequiredMixin, FormView):
    template_name = 'apps/surveys/pregunta_dos.html'
    form_class = PreguntaDosForm
    model = PreguntaDos
    login_url = 'users_app:user-login'  # URL de inicio de sesión

    def form_valid(self, form):
        pregunta_dos = form.save(commit=False)
        pregunta_dos.usuario = self.request.user
        pregunta_dos.save()

        return redirect('surveys_app:pregunta_cinco')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        usuario = self.request.user
        try:
            pregunta_dos = PreguntaDos.objects.get(usuario=usuario)
            context['propuesta_1_guardada'] = pregunta_dos.propuesta_1
            context['propuesta_2_guardada'] = pregunta_dos.propuesta_2
            context['propuesta_3_guardada'] = pregunta_dos.propuesta_3
            context['propuesta_4_guardada'] = pregunta_dos.propuesta_4
        except PreguntaDos.DoesNotExist:
            context['propuesta_1_guardada'] = None
            context['propuesta_2_guardada'] = None
            context['propuesta_3_guardada'] = None
            context['propuesta_4_guardada'] = None
        return context


class PreguntaTresView(LoginRequiredMixin, FormView):
    template_name = 'apps/surveys/pregunta_tres.html'


class PreguntaCincoView(LoginRequiredMixin, FormView):
    template_name = 'apps/surveys/pregunta_cinco.html'
    form_class = PreguntaCincoForm
    model = PreguntaCinco
    login_url = 'users_app:user-login'  # URL de inicio de sesión

    def form_valid(self, form):
        pregunta_cinco = form.save(commit=False)
        pregunta_cinco.usuario = self.request.user

        # recoger los datos del formulario de la sesión
        pregunta_uno_data = self.request.session.get('pregunta_uno_data')
        pregunta_dos_data = self.request.session.get('pregunta_dos_data')

        # validar los datos del formulario y guardarlos en la base de datos si son válidos
        if pregunta_uno_data is not None and pregunta_dos_data is not None:
            pregunta_uno_form = PreguntaUnoForm(pregunta_uno_data)
            pregunta_dos_form = PreguntaDosForm(pregunta_dos_data)
            if pregunta_uno_form.is_valid() and pregunta_dos_form.is_valid():
                pregunta_uno = pregunta_uno_form.save(commit=False)
                pregunta_uno.usuario = self.request.user
                pregunta_uno.save()

                pregunta_dos = pregunta_dos_form.save(commit=False)
                pregunta_dos.usuario = self.request.user
                pregunta_dos.save()

                pregunta_cinco.save()

                return redirect('surveys_app:enviar_formularios')

        # si los datos del formulario no son válidos o no están disponibles, redirigir al usuario a la primera página del formulario
        return redirect('surveys_app:pregunta_uno')

    def form_invalid(self, form):
        return JsonResponse(form.errors, status=400)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        usuario = self.request.user
        try:
            pregunta_cinco = PreguntaCinco.objects.get(usuario=usuario)
            context['valor_guardado'] = pregunta_cinco.texto_respuesta
        except PreguntaCinco.DoesNotExist:
            context['valor_guardado'] = None

        session = SessionStore()
        pregunta_uno_valor = session.get('pregunta_uno_valor')
        pregunta_dos_propuesta_1 = session.get('pregunta_dos_propuesta_1')
        pregunta_dos_propuesta_2 = session.get('pregunta_dos_propuesta_2')
        pregunta_dos_propuesta_3 = session.get('pregunta_dos_propuesta_3')
        pregunta_dos_propuesta_4 = session.get('pregunta_dos_propuesta_4')

        context['pregunta_uno_valor'] = pregunta_uno_valor
        context['pregunta_dos_propuesta_1'] = pregunta_dos_propuesta_1
        context['pregunta_dos_propuesta_2'] = pregunta_dos_propuesta_2
        context['pregunta_dos_propuesta_3'] = pregunta_dos_propuesta_3
        context['pregunta_dos_propuesta_4'] = pregunta_dos_propuesta_4

        return context


class EnviarFormulariosViews(LoginRequiredMixin, TemplateView):
    template_name = 'apps/surveys/enviar_formularios.html'
    login_url = 'users_app:user-login'  # URL de inicio de sesión
