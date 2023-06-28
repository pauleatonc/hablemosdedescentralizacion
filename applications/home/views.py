from django.views.generic import TemplateView

# importar modelos
from . models import Countdown

# importar apps de terceros


class HomePageView(TemplateView):
    template_name = 'apps/home/home.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        countdown = Countdown.objects.first()  # Obtén el objeto Countdown deseado aquí creado en la base de datos
        context['countdown'] = countdown
        return context


class Error404(TemplateView):
    template_name = 'home/404.html'

    
class Error500(TemplateView):
    template_name = "home/500.html"

    @classmethod
    def as_error_view(cls):

        v = cls.as_view()
        def view(request):
            r = v(request)
            r.render()
            return r
        return view


class Error503(TemplateView):
    template_name = 'home/503.html'

    @classmethod
    def as_error_view(cls):
        v = cls.as_view()

        def view(request):
            r = v(request)
            r.render()
            return r

        return view

    