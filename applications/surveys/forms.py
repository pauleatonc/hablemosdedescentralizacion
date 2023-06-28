from django import forms

from .models import Respuesta, PreguntaUno


class PreguntaUnoForm(forms.ModelForm):
    class Meta:
        model = PreguntaUno
        fields = ('valor',)

        widgets = {
            'valor': forms.Select(attrs={'class': 'form-control'}),
        }


class PreguntaDosForm(forms.ModelForm):
    class Meta:
        model = Respuesta
        fields = ['pregunta_dos']


class PreguntaTresForm(forms.ModelForm):
    class Meta:
        model = Respuesta
        fields = ['pregunta_tres']


class PreguntaCincoForm(forms.ModelForm):
    class Meta:
        model = Respuesta
        fields = ['pregunta_cinco']