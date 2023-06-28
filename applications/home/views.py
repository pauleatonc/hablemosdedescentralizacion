from django.shortcuts import render
from django.conf import settings
from django.urls import reverse_lazy
from django.views.generic import View, TemplateView, CreateView
from django.http import  HttpResponseServerError

# importar modelos


# importar apps de terceros


class HomePageView(TemplateView):
    template_name = 'apps/home/home.html'


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

    