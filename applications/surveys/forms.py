from django import forms

from .models import PreguntaUno, PreguntaDos, PreguntaCinco


class PreguntaUnoForm(forms.ModelForm):
    class Meta:
        model = PreguntaUno
        fields = ('valor',)

        widgets = {
            'valor': forms.Select(attrs={'class': 'form-control'}),
        }


class PreguntaDosForm(forms.ModelForm):
    class Meta:
        model = PreguntaDos
        fields = ['propuesta_1', 'propuesta_2', 'propuesta_3', 'propuesta_4']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        opciones = [(i, str(i)) for i in range(1, 5)]  # Generar opciones del 1 al 4
        for i in range(1, 5):
            self.fields[f'propuesta_{i}'].widget = forms.Select(choices=opciones)


class PreguntaCincoForm(forms.ModelForm):
    class Meta:
        model = PreguntaCinco
        fields = ['texto_respuesta']

        widgets = {
            'texto_respuesta': forms.Textarea(attrs={'required': False, 'placeholder': 'Escribe aquí tu respuesta.'})
        }
