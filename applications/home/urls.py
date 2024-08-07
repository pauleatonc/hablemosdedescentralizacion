from django.urls import path
from .views import generar_reporte_completo

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
        name='politicas_privacidad',
        ),

    path(
        'onboarding',
        views.OnboardingView.as_view(),
        name='onboarding',
    ),

    path(
        'descentralizacion_para_bienestar',
        views.DescentralizacionBienestarView.as_view(),
        name='descentralizacion-bienestar',
    ),
    path(
        'consejo_asesor',
        views.ConsejoAsesorListView.as_view(),
        name='consejo-asesor',
    ),
    path(
        'calendario_dialogos',
        views.CalendarioDialogosView.as_view(),
        name='calendario_dialogos',
    ),
     path(
         'generar_reporte_completo/', 
         generar_reporte_completo, 
         name='generar_reporte_completo'
    ),

]
