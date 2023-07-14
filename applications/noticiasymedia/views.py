from django.shortcuts import render
from applications.noticiasymedia.models import Noticias, Multimedia
from django.views.generic import View, TemplateView

# Create your views here.
class NoticiasView(TemplateView):
    template_name = 'apps/noticiasymedia/noticias.html'
    model = Noticias
    
class MultimediaView(TemplateView):
    template_name = 'apps/noticiasymedia/multimedia.html'
    model = Multimedia


class NoticiasDetailView(TemplateView):
    template_name = 'apps/noticiasymedia/noticia_detail.html'
    model = Noticias
    
class MultimediaDetailView(TemplateView):
    template_name = 'apps/noticiasymedia/media_detail.html'
    model = Multimedia
    
