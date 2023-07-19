from django.shortcuts import render
from applications.noticiasymedia.models import Noticias, Multimedia
from django.views.generic import  TemplateView, DetailView
from django.core.paginator import Paginator 

# Create your views here.
class NoticiasView(TemplateView):
    template_name = 'apps/noticiasymedia/noticias.html'
    paginate_by=6
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        noticias = Noticias.objects.all()
        paginator = Paginator(noticias, self.paginate_by)
        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context['noticias']= page_obj
        
        return context    
    


class NoticiaDetailView(DetailView):
    template_name = 'apps/noticiasymedia/noticia_detail.html'
    model = Noticias
    context_object_name = 'noticia'
    
class MultimediaView(TemplateView):
    template_name = 'apps/noticiasymedia/multimedia.html'
    model = Multimedia
class MultimediaDetailView(TemplateView):
    template_name = 'apps/noticiasymedia/media_detail.html'
    model = Multimedia
    
