from django.urls import path

from . import views

app_name = 'surveys_app'

urlpatterns = [

    path('comunas_por_region/<int:region_id>/', views.ComunasPorRegionView.as_view(), name='comunas_por_region'),
    path('consulta-datos-usuario/', views.ConsultaDatosUsuarioView.as_view(), name='consulta_datos_usuario'),
    path('pregunta-uno/', views.PreguntaUnoView.as_view(), name='pregunta_uno'),
    path('pregunta-dos/', views.PreguntaDosView.as_view(), name='pregunta_dos'),
    path('pregunta-tres/', views.PreguntaTresView.as_view(), name='pregunta_tres'),
    path('pregunta-cuatro/', views.PreguntaCuatroView.as_view(), name='pregunta_cuatro'),
    path('pregunta-cinco/', views.PreguntaCincoView.as_view(), name='pregunta_cinco'),
    path('pregunta-seis/', views.PreguntaSeisView.as_view(), name='pregunta_seis'),
    path('pregunta-siete/', views.PreguntaSieteView.as_view(), name='pregunta_siete'),
    path('enviar-formularios/', views.EnviarFormulariosViews.as_view(), name='enviar_formularios'),
    path('resumen-encuesta/', views.ResumenRespuestasUsuarioView.as_view(), name='resumen_encuesta')
    
]
