from django import forms
from django.core.exceptions import ValidationError

from .models import PreguntaUno, PreguntaDos, PreguntaCinco


class PreguntaUnoForm(forms.ModelForm):

    valor = forms.ChoiceField(choices=PreguntaUno.VALORES, required=True)

    class Meta:
        model = PreguntaUno
        fields = ['valor']
        widgets = {
            'valor': forms.RadioSelect
        }

    def clean(self):
        cleaned_data = super().clean()
        valor = cleaned_data.get('valor')
        if not valor:
            raise ValidationError('Debes elegir una opción antes de continuar.')
        return cleaned_data


class PreguntaDosForm(forms.ModelForm):
    class Meta:
        model = PreguntaDos
        fields = ('propuesta_1', 'propuesta_2', 'propuesta_3', 'propuesta_4')
        widgets = {
            'propuesta_1': forms.NumberInput(
                attrs={
                    'required': True,
                    'placeholder': '-',
                    'class': 'propuesta',
                    'id': 'propuesta_1'
                }
            ),
            'propuesta_2': forms.NumberInput(
                attrs={
                    'required': True,
                    'placeholder': '-',
                    'class': 'propuesta',
                    'id': 'propuesta_2'
                }
            ),
            'propuesta_3': forms.NumberInput(
                attrs={
                    'required': True,
                    'placeholder': '-',
                    'class': 'propuesta',
                    'id': 'propuesta_3'
                }
            ),
            'propuesta_4': forms.NumberInput(
                attrs={
                    'required': True,
                    'placeholder': '-',
                    'class': 'propuesta',
                    'id': 'propuesta_4'
                }
            ),
        }

    def clean(self):
        cleaned_data = super().clean()

        valores = [
            cleaned_data.get('propuesta_1'),
            cleaned_data.get('propuesta_2'),
            cleaned_data.get('propuesta_3'),
            cleaned_data.get('propuesta_4'),
        ]

        # Verificar que todos los campos estén presentes
        if None in valores:
            raise forms.ValidationError('Todos los campos son requeridos.')

        return cleaned_data


class PreguntaCincoForm(forms.ModelForm):
    class Meta:
        model = PreguntaCinco
        fields = ['texto_respuesta']

        widgets = {
            'texto_respuesta': forms.Textarea(attrs={'required': False, 'placeholder': 'Escribe aquí tu respuesta.'})
        }
