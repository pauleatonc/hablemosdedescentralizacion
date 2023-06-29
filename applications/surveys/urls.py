from django.urls import path

from . import views

app_name = 'surveys_app'

urlpatterns = [

    path('pregunta-uno/', views.PreguntaUnoView.as_view(), name='pregunta_uno'),
    path('pregunta-dos/', views.PreguntaDosView.as_view(), name='pregunta_dos'),
    path('pregunta-tres/', views.PreguntaTresView.as_view(), name='pregunta_tres'),
    path('pregunta-cinco/', views.PreguntaCincoView.as_view(), name='pregunta_cinco'),
    path('enviar-formularios/', views.EnviarFormulariosViews.as_view(), name='enviar_formularios'),
    
]