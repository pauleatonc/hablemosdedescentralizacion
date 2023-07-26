from django.urls import path

from . import views
from .views import  NoticiaDetailView

app_name = 'noticiasymedia_app'

urlpatterns = [
    path('noticias/', views.NoticiasView.as_view(), name='noticias'),
    path('multimedia/', views.MultimediaView.as_view(), name='multimedia'),
    path('noticias/<slug>/', NoticiaDetailView.as_view(), name='noticia_detail'),
    path('multimedia/<slug>/', views.MultimediaDetailView.as_view(), name='multimedia_detail'),
]
