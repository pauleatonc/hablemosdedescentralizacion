from django.views.generic import TemplateView
from .forms import PreguntaUnoForm, PreguntaDosForm, PreguntaTresForm, PreguntaCincoForm


class PreguntaUnoView(TemplateView):
    template_name = 'apps/surveys/pregunta_uno.html'
    form_class = PreguntaUnoForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.form_class()
        return context


class PreguntaDosView(TemplateView):
    template_name = 'apps/surveys/pregunta_dos.html'
    form_class = PreguntaDosForm


class PreguntaTresView(TemplateView):
    template_name = 'apps/surveys/pregunta_tres.html'
    form_class = PreguntaTresForm


class PreguntaCincoView(TemplateView):
    template_name = 'apps/surveys/pregunta_cinco.html'
    form_class = PreguntaCincoForm

