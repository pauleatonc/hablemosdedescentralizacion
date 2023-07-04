from django.urls import path

from . import views

app_name = 'home_app'

urlpatterns = [
    path(
        '',
        views.HomePageView.as_view(),
        name='index',
        ),

     path(
        'preguntas-frecuentes',
        views.PreguntasFrecuentesView.as_view(),
        name='preguntas_frecuentes',
        ),

    path(
        'documentos',
        views.DocumentosView.as_view(),
        name='documentos',
        ),
        
]