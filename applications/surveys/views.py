from django.views.generic import TemplateView, View
from .forms import (
    PreguntaUnoForm,
    PreguntaDosForm,
    PreguntaTresForm,
    # PreguntaCuatroForm,
    PreguntaCincoForm,
    PreguntaSeisForm,
    PreguntaSieteForm,
    DatosUsuarioForm,
    EnviarFormulariosForm
)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.views.generic.edit import FormView
from .models import PreguntaUno, PreguntaDos, PreguntaTres, PreguntaCinco, OpcionesPreguntaCinco, PreguntaSeis, PreguntaSiete
from applications.regioncomuna.models import Region, Comuna
from applications.users.models import User
from django.http import JsonResponse
from .functions import send_email
from django.conf import settings
from django.template.loader import render_to_string
from django.forms.models import model_to_dict



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

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({
            'instance': self.request.user
        })
        return kwargs

    def get(self, request, *args, **kwargs):
        usuario = self.request.user

        if usuario.encuesta_completada:
            return redirect('surveys_app:enviar_formularios')

        return super().get(request, *args, **kwargs)

    def form_valid(self, form):
        form.save()
        return redirect('surveys_app:pregunta_uno')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['regiones'] = Region.objects.all()
        usuario = self.request.user
        if usuario.comuna is not None:
            try:
                context['region_guardada'] = usuario.comuna.region
                context['comuna_guardada'] = usuario.comuna
            except AttributeError:
                context['region_guardada'] = None
                context['comuna_guardada'] = None
        else:
            context['region_guardada'] = None
            context['comuna_guardada'] = None
        try:
            context['genero_guardada'] = usuario.get_genero_display()
            context['edad_guardada'] = usuario.edad
            context['pueblo_originario_guardado'] = usuario.get_pueblo_originario_display()
            context['politica_privacidad_guardada'] = usuario.politica_privacidad
        except AttributeError:
            context['genero_guardada'] = None
            context['edad_guardada'] = None
            context['pueblo_originario_guardado'] = None
            context['politica_privacidad_guardada'] = None
        return context


class PreguntaUnoView(LoginRequiredMixin, FormView):
    template_name = 'apps/surveys/pregunta_uno.html'
    form_class = PreguntaUnoForm
    model = PreguntaUno
    login_url = 'users_app:user-login'  # URL de inicio de sesión

    def get(self, request, *args, **kwargs):
        usuario = self.request.user

        if usuario.encuesta_completada:
            return redirect('surveys_app:enviar_formularios')

        return super().get(request, *args, **kwargs)

    def form_valid(self, form):
        usuario = self.request.user
        try:
            pregunta_uno = PreguntaUno.objects.get(usuario=usuario)
        except PreguntaUno.DoesNotExist:
            pregunta_uno = PreguntaUno(usuario=usuario)
        pregunta_uno.valor = form.cleaned_data.get('valor')
        pregunta_uno.save()
        return redirect('surveys_app:pregunta_dos')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        usuario = self.request.user
        try:
            pregunta_uno = PreguntaUno.objects.get(usuario=usuario)
            context['valor_guardado'] = pregunta_uno.valor  # Esto obtendrá la clave, no la etiqueta.
        except PreguntaUno.DoesNotExist:
            context['valor_guardado'] = None
        return context


class PreguntaDosView(LoginRequiredMixin, FormView):
    template_name = 'apps/surveys/pregunta_dos.html'
    form_class = PreguntaDosForm
    model = PreguntaDos
    login_url = 'users_app:user-login'  # URL de inicio de sesión

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({'request': self.request})
        return kwargs

    def get(self, request, *args, **kwargs):
        usuario = self.request.user

        if usuario.encuesta_completada:
            return redirect('surveys_app:enviar_formularios')

        try:
            pregunta_dos = PreguntaDos.objects.get(usuario=usuario)
            form = self.form_class(initial={
                'propuesta_1': pregunta_dos.propuesta_1,
                'propuesta_2': pregunta_dos.propuesta_2,
                'propuesta_3': pregunta_dos.propuesta_3,
                'propuesta_4': pregunta_dos.propuesta_4,
            }, request=request)
        except PreguntaDos.DoesNotExist:
            form = self.form_class(request=request)

        return self.render_to_response(self.get_context_data(form=form))

    def form_valid(self, form):
        usuario = self.request.user
        try:
            pregunta_dos = PreguntaDos.objects.get(usuario=usuario)
        except PreguntaDos.DoesNotExist:
            pregunta_dos = PreguntaDos(usuario=usuario)
        pregunta_dos.propuesta_1 = form.cleaned_data.get('propuesta_1')
        pregunta_dos.propuesta_2 = form.cleaned_data.get('propuesta_2')
        pregunta_dos.propuesta_3 = form.cleaned_data.get('propuesta_3')
        pregunta_dos.propuesta_4 = form.cleaned_data.get('propuesta_4')
        pregunta_dos.save()

        return redirect('surveys_app:pregunta_tres')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        usuario = self.request.user
        try:
            pregunta_dos = PreguntaDos.objects.get(usuario=usuario)
            context['propuesta_1_guardada'] = pregunta_dos.propuesta_1
        except PreguntaDos.DoesNotExist:
            context['propuesta_1_guardada'] = None
        return context


class PreguntaTresView(LoginRequiredMixin, FormView):
    template_name = 'apps/surveys/pregunta_tres.html'
    form_class = PreguntaTresForm
    model = PreguntaTres
    login_url = 'users_app:user-login'  # URL de inicio de sesión

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({'request': self.request})
        return kwargs
    
    def get(self, request, *args, **kwargs):
        usuario = self.request.user

        if usuario.encuesta_completada:
            return redirect('surveys_app:enviar_formularios')

        try:
            pregunta_tres = PreguntaTres.objects.get(usuario=usuario)
            form = self.form_class(initial={
                'iniciativa_1': pregunta_tres.iniciativa_1,
                'iniciativa_2': pregunta_tres.iniciativa_2,
                'iniciativa_3': pregunta_tres.iniciativa_3,
                'iniciativa_4': pregunta_tres.iniciativa_4,
                'iniciativa_5': pregunta_tres.iniciativa_5,
            }, request=request)
        except PreguntaTres.DoesNotExist:
            form = self.form_class(request=request)

        return self.render_to_response(self.get_context_data(form=form))

    def form_valid(self, form):
        usuario = self.request.user
        try:
            pregunta_tres = PreguntaTres.objects.get(usuario=usuario)
        except PreguntaTres.DoesNotExist:
            pregunta_tres = PreguntaTres(usuario=usuario)
        pregunta_tres.iniciativa_1 = form.cleaned_data.get('iniciativa_1')
        pregunta_tres.iniciativa_2 = form.cleaned_data.get('iniciativa_2')
        pregunta_tres.iniciativa_3 = form.cleaned_data.get('iniciativa_3')
        pregunta_tres.iniciativa_4 = form.cleaned_data.get('iniciativa_4')
        pregunta_tres.iniciativa_5 = form.cleaned_data.get('iniciativa_5')
        pregunta_tres.save()

        return redirect('surveys_app:pregunta_cinco')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        usuario = self.request.user
        try:
            pregunta_tres = PreguntaTres.objects.get(usuario=usuario)
            context['iniciativa_1_guardada'] = pregunta_tres.iniciativa_1
        except PreguntaTres.DoesNotExist:
            context['iniciativa_1_guardada'] = None
        return context


# class PreguntaCuatroView(LoginRequiredMixin, FormView):
#     template_name = 'apps/surveys/pregunta_cuatro.html'
#     form_class = PreguntaCuatroForm
#     model = PreguntaCuatro
#     login_url = 'users_app:user-login'  # URL de inicio de sesión

#     def get_form_kwargs(self):
#         kwargs = super().get_form_kwargs()
#         kwargs.update({'request': self.request})
#         return kwargs

#     def get(self, request, *args, **kwargs):
#         usuario = self.request.user

#         if usuario.encuesta_completada:
#             return redirect('surveys_app:enviar_formularios')

#         try:
#             pregunta_cuatro = PreguntaCuatro.objects.get(usuario=usuario)
#             form = self.form_class(initial={
#                 'tematica_1': pregunta_cuatro.tematica_1,
#                 'tematica_2': pregunta_cuatro.tematica_2,
#                 'tematica_3': pregunta_cuatro.tematica_3,
#                 'tematica_4': pregunta_cuatro.tematica_4,
#                 'tematica_5': pregunta_cuatro.tematica_5,
#             }, request=request)
#         except PreguntaCuatro.DoesNotExist:
#             form = self.form_class(request=request)

#         return self.render_to_response(self.get_context_data(form=form))

#     def form_valid(self, form):
#         usuario = self.request.user
#         try:
#             pregunta_cuatro = PreguntaCuatro.objects.get(usuario=usuario)
#         except PreguntaCuatro.DoesNotExist:
#             pregunta_cuatro = PreguntaCuatro(usuario=usuario)
#         pregunta_cuatro.tematica_1 = form.cleaned_data.get('tematica_1')
#         pregunta_cuatro.tematica_2 = form.cleaned_data.get('tematica_2')
#         pregunta_cuatro.tematica_3 = form.cleaned_data.get('tematica_3')
#         pregunta_cuatro.tematica_4 = form.cleaned_data.get('tematica_4')
#         pregunta_cuatro.tematica_5 = form.cleaned_data.get('tematica_5')
#         pregunta_cuatro.save()

#         return redirect('surveys_app:pregunta_cinco')
    
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         usuario = self.request.user
#         try:
#             pregunta_cuatro = PreguntaCuatro.objects.get(usuario=usuario)
#             context['tematica_1_guardada'] = pregunta_cuatro.get_tematica_1_display()

#         except PreguntaCuatro.DoesNotExist:
#             context['tematica_1_guardada'] = None

#         return context


class PreguntaCincoView(LoginRequiredMixin, FormView):
    template_name = 'apps/surveys/pregunta_cinco.html'
    form_class = PreguntaCincoForm
    model = PreguntaCinco
    login_url = 'users_app:user-login'  # URL de inicio de sesión

    def get(self, request, *args, **kwargs):
        usuario = self.request.user

        if usuario.encuesta_completada:
            return redirect('surveys_app:enviar_formularios')

        try:
            pregunta_cinco = PreguntaCinco.objects.get(usuario=usuario)
            form = self.form_class(instance=pregunta_cinco)
            initial_opciones = list(pregunta_cinco.opciones.values_list('id', flat=True))
        except PreguntaCinco.DoesNotExist:
            form = self.form_class()
            initial_opciones = []

        opciones = OpcionesPreguntaCinco.objects.all()
        return self.render_to_response(self.get_context_data(form=form, opciones=opciones, initial_opciones=initial_opciones))

    def post(self, request, *args, **kwargs):
        usuario = self.request.user
        
        # Transformar 'opciones' en una lista de IDs
        post_data = request.POST.copy()
        if 'opciones' in post_data:
            post_data.setlist('opciones', post_data['opciones'].split(','))

        form = self.form_class(post_data)
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        usuario = self.request.user

        # Get or create the PreguntaCinco instance
        pregunta_cinco, created = PreguntaCinco.objects.get_or_create(usuario=usuario)

        # Set the selected options
        opciones_seleccionadas = form.cleaned_data['opciones']
        
        pregunta_cinco.opciones.set(opciones_seleccionadas)
        pregunta_cinco.save()

        usuario.save()

        return redirect('surveys_app:pregunta_seis')

    def form_invalid(self, form):
        print("Form is invalid.")
        print(form.errors)
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        usuario = self.request.user
        try:
            pregunta_cinco = PreguntaCinco.objects.get(usuario=usuario)
            context['form'] = self.form_class(instance=pregunta_cinco)
        except PreguntaCinco.DoesNotExist:
            context['form'] = self.form_class()
        context['opciones'] = OpcionesPreguntaCinco.objects.all()
        context['initial_opciones'] = kwargs.get('initial_opciones', [])
        return context


class PreguntaSeisView(LoginRequiredMixin, FormView):
    template_name = 'apps/surveys/pregunta_seis.html'
    form_class = PreguntaSeisForm
    model = PreguntaSeis
    login_url = 'users_app:user-login'  # URL de inicio de sesión

    def get(self, request, *args, **kwargs):
        usuario = self.request.user

        if usuario.encuesta_completada:
            return redirect('surveys_app:enviar_formularios')

        return super().get(request, *args, **kwargs)

    def form_valid(self, form):
        usuario = self.request.user
        try:
            pregunta_seis = PreguntaSeis.objects.get(usuario=usuario)
        except PreguntaSeis.DoesNotExist:
            pregunta_seis = PreguntaSeis(usuario=usuario)
        pregunta_seis.valor = form.cleaned_data.get('valor')
        pregunta_seis.save()
        return redirect('surveys_app:pregunta_siete')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        usuario = self.request.user
        try:
            pregunta_seis = PreguntaSeis.objects.get(usuario=usuario)
            context['valor_guardado'] = pregunta_seis.valor  # Esto obtendrá la clave, no la etiqueta.
        except PreguntaSeis.DoesNotExist:
            context['valor_guardado'] = None
        return context
    

class PreguntaSieteView(LoginRequiredMixin, FormView):
    template_name = 'apps/surveys/pregunta_siete.html'
    form_class = PreguntaSieteForm
    model = PreguntaSiete
    login_url = 'users_app:user-login'  # URL de inicio de sesión

    def get(self, request, *args, **kwargs):
        usuario = self.request.user

        if usuario.encuesta_completada:
            return redirect('surveys_app:enviar_formularios')

        try:
            pregunta_siete = PreguntaSiete.objects.get(usuario=usuario)
            form = self.form_class(initial={
                'texto_respuesta': pregunta_siete.texto_respuesta,
            })
        except PreguntaSiete.DoesNotExist:
            form = self.form_class()

        return self.render_to_response(self.get_context_data(form=form))

    def form_valid(self, form):
        usuario = self.request.user
        try:
            pregunta_siete = PreguntaSiete.objects.get(usuario=usuario)
        except PreguntaSiete.DoesNotExist:
            pregunta_siete = PreguntaSiete(usuario=usuario)
        pregunta_siete.texto_respuesta = form.cleaned_data.get('texto_respuesta')
        pregunta_siete.save()

        usuario.encuesta_completada = True
        usuario.save()

        return redirect('surveys_app:enviar_formularios')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        usuario = self.request.user
        try:
            pregunta_siete = PreguntaSiete.objects.get(usuario=usuario)
            context['valor_guardado'] = pregunta_siete.texto_respuesta
        except PreguntaSiete.DoesNotExist:
            context['valor_guardado'] = None

        return context


class EnviarFormulariosViews(LoginRequiredMixin, FormView):
    template_name = 'apps/surveys/enviar_formularios.html'
    form_class = EnviarFormulariosForm
    login_url = 'users_app:user-login'  # URL de inicio de sesión

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({
            'instance': self.request.user
        })
        return kwargs

    def form_valid(self, form):
        # Guardar el formulario y obtener la instancia del modelo
        self.object = form.save()

        # Obtener datos del formulario
        email = form.cleaned_data['email']
        recibir_resultados = form.cleaned_data['recibir_resultados']

        self.success_url = self.request.path

        # Obtener el usuario actual
        usuario = self.request.user

        pregunta_uno = PreguntaUno.objects.get(usuario=usuario)
        pregunta_dos = PreguntaDos.objects.get(usuario=usuario)
        pregunta_tres = PreguntaTres.objects.get(usuario=usuario)
        pregunta_cinco = PreguntaCinco.objects.get(usuario=usuario)
        pregunta_seis = PreguntaSeis.objects.get(usuario=usuario)
        pregunta_siete = PreguntaSiete.objects.get(usuario=usuario)

        pregunta_dos_list = []
        for field in pregunta_dos._meta.fields:
            if field.name.startswith('propuesta_'):
                pregunta_dos_list.append(
                    (field.help_text, getattr(pregunta_dos, f'get_{field.name}_display')()))

        pregunta_tres_list = []
        for field in pregunta_tres._meta.fields:
            if field.name.startswith('iniciativa_'):
                pregunta_tres_list.append(
                    (field.help_text, getattr(pregunta_tres, f'get_{field.name}_display')()))

        # pregunta_cuatro_list = []
        # for field in pregunta_cuatro._meta.fields:
        #     if field.name.startswith('tematica_'):
        #         pregunta_cuatro_list.append(
        #             (field.verbose_name, field.help_text, getattr(pregunta_cuatro, f'get_{field.name}_display')()))

        context = {
            'respuesta_uno': pregunta_uno.get_valor_display(),
            'pregunta_dos': pregunta_dos_list,
            'pregunta_tres': pregunta_tres_list,
            # 'pregunta_cuatro': pregunta_cuatro_list,
            'pregunta_cinco': pregunta_cinco.get_opciones_texto(),
            'respuesta_seis': pregunta_seis.get_valor_display(),
            'respuesta_siete': pregunta_siete.texto_respuesta,
        }

        # Renderizar la plantilla con el contexto y obtener una cadena HTML
        content = render_to_string('apps/surveys/resumen_respuestas_usuario.html', context)

        admin_email = settings.ADMIN_EMAIL

        # Enviar el correo electrónico con los datos del formulario
        send_email(
            'Resultados de la encuesta - Banco de Proyectos',  # Asunto
            content,  # Contenido HTML
            admin_email,  # Email del remitente
            [email]  # Email del destinatario
        )

        return super().form_valid(form)


class ResumenRespuestasUsuarioView(LoginRequiredMixin, TemplateView):
    template_name = 'apps/surveys/resumen_respuestas_usuario.html'

    def get_context_data(self, **kwargs):
        usuario = self.request.user

        pregunta_uno = PreguntaUno.objects.get(usuario=usuario)
        pregunta_dos = PreguntaDos.objects.get(usuario=usuario)
        pregunta_tres = PreguntaTres.objects.get(usuario=usuario)
        # pregunta_cuatro = PreguntaCuatro.objects.get(usuario=usuario)
        pregunta_cinco = PreguntaCinco.objects.get(usuario=usuario)
        pregunta_seis = PreguntaSeis.objects.get(usuario=usuario)
        pregunta_siete = PreguntaSiete.objects.get(usuario=usuario)

        pregunta_dos_list = []
        for field in pregunta_dos._meta.fields:
            if field.name.startswith('propuesta_'):
                pregunta_dos_list.append(
                    (field.help_text, getattr(pregunta_dos, f'get_{field.name}_display')()))

        pregunta_tres_list = []
        for field in pregunta_tres._meta.fields:
            if field.name.startswith('iniciativa_'):
                pregunta_tres_list.append(
                    (field.help_text, getattr(pregunta_tres, f'get_{field.name}_display')()))

        # pregunta_cuatro_list = []
        # for field in pregunta_cuatro._meta.fields:
        #     if field.name.startswith('tematica_'):
        #         pregunta_cuatro_list.append((field.verbose_name, field.help_text, getattr(pregunta_cuatro, f'get_{field.name}_display')()))


        context = {
                'respuesta_uno': pregunta_uno.get_valor_display(),
                'pregunta_dos': pregunta_dos_list,
                'pregunta_tres': pregunta_tres_list,
                # 'pregunta_cuatro': pregunta_cuatro_list,
                'pregunta_cinco': pregunta_cinco.get_opciones_texto(),
                'respuesta_seis': pregunta_seis.get_valor_display(),
                'respuesta_siete': pregunta_siete.texto_respuesta,
            }

        return context