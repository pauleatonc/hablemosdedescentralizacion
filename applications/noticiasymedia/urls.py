from django.urls import path

from . import views
from .views import  NoticiaDetailView, LatestAlbumsByRegionView, AlbumsByRegionView, FileFieldFormView

app_name = 'noticiasymedia_app'

urlpatterns = [
    path('noticias/', views.NoticiasView.as_view(), name='noticias'),
    path('multimedia/', views.MultimediaView.as_view(), name='multimedia'),
    path('noticias/<slug>/', NoticiaDetailView.as_view(), name='noticia_detail'),
    path('multimedia/<slug>/', views.MultimediaDetailView.as_view(), name='multimedia_detail'),
    path('fotos/', LatestAlbumsByRegionView.as_view(), name='albums'),
    path('fotos/<int:region_id>/', AlbumsByRegionView.as_view(), name='albums_by_region'),
    path('upload_photos/', FileFieldFormView.as_view(), name='upload_photos'),
]
