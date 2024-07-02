from typing import Any, Dict
from django.shortcuts import render
from applications.noticiasymedia.models import Noticias, Multimedia, PhotoAlbum, Photo
from django.views.generic import TemplateView, DetailView, ListView
from django.core.paginator import Paginator
from django.db.models import Max

from applications.regioncomuna.models import Region
from django.db import models


class NoticiasView(TemplateView):
    template_name = 'apps/noticiasymedia/noticias.html'
    paginate_by = 6
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        noticias = Noticias.objects.all()
        paginator = Paginator(noticias, self.paginate_by)
        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context['noticias'] = page_obj
        
        return context    


class NoticiaDetailView(DetailView):
    template_name = 'apps/noticiasymedia/noticia_detail.html'
    model = Noticias
    context_object_name = 'noticia'

    
class MultimediaView(TemplateView):
    template_name = 'apps/noticiasymedia/multimedia.html'
    paginate_by = 6 
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        multimedias = Multimedia.objects.all()
        paginator = Paginator(multimedias, self.paginate_by)
        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context['multimedias'] = page_obj
        
        return context


class MultimediaDetailView(DetailView):
    template_name = 'apps/noticiasymedia/media_detail.html'
    model = Multimedia
    context_object_name = 'multimedia'


class LatestAlbumsByRegionView(TemplateView):
    template_name = 'apps/noticiasymedia/album.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        regions_with_latest_album_date = Region.objects.annotate(
            latest_album_date=Max('photoalbum__date')
        ).order_by('id')  # Ordena las regiones por nombre

        latest_albums = []
        for region in regions_with_latest_album_date:
            latest_album = PhotoAlbum.objects.filter(
                region=region,
                date=region.latest_album_date,
                publie=True
            ).order_by('-date').first()  # Asegúrate de que también aquí se ordena por fecha si es necesario
            if latest_album:
                latest_albums.append(latest_album)

        context['albums'] = latest_albums
        return context


class LatestAlbumsHome(TemplateView):
    paginate_by = 3  # Define cuántos elementos por página quieres mostrar

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Ordenar todos los álbumes por fecha de última modificación
        all_albums = PhotoAlbum.objects.filter(
            public=True  # Añadir filtro para mostrar solo álbumes públicos
        ).order_by('-modified')

        # Aplicar la paginación
        paginator = Paginator(all_albums, self.paginate_by)
        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        context['latest_albums'] = page_obj
        return context


class AlbumsByRegionView(ListView):
    model = PhotoAlbum
    template_name = 'apps/noticiasymedia/albums_by_region.html'
    context_object_name = 'albums'

    def get_queryset(self):
        region_id = self.kwargs['region_id']
        return PhotoAlbum.objects.filter(
            region_id=region_id,
            public=True  # Añadir filtro para mostrar solo álbumes públicos
        ).order_by('-date')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        region = Region.objects.get(pk=self.kwargs['region_id'])
        context['region_name'] = region.region
        return context
