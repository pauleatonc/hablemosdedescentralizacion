from django.urls import path

from . import views

app_name = 'noticiasymedia_app'

urlpatterns = [
    path('noticias/',views.NoticiasView.as_view(), name='noticias'), 
    path('multimedia/',views.MultimediaView.as_view(), name='multimedia'), 
    path('noticias/<pk>/',views.NoticiasDetailView.as_view(), name='detalle noticia'), 
    path('multimedia/<pk>/',views.MultimediaDetailView.as_view(), name='detalle multimedia'), 
]
