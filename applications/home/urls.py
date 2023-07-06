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
        'proceso-participativo',
        views.ProcesoParticipativoView.as_view(),
        name='proceso_participativo',
        ),

     path(
        'preguntas-frecuentes',
        views.PreguntasFrecuentesView.as_view(),
        name='preguntas_frecuentes',
        ),

    path(
        'documentos/',
        views.DocumentosView.as_view(),
        name='documentos',
        ),

    path(
        'politicas-privacidad',
        views.PoliticasPrivacidadView.as_view(),
        name='politivas_privacidad',
        ),

        path(
        'onboarding',
        views.OnboardingView.as_view(),
        name='onboarding',
        ),

]