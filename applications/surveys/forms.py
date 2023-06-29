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
        fields = ('propuesta_1', 'propuesta_2', 'propuesta_3', 'propuesta_4')
        widgets = {
            'propuesta_1': forms.Select(
                attrs={
                    'required': True,
                    'placeholder': '-',
                    'class': 'custom-input'
                }
            ),
            'propuesta_2': forms.Select(
                attrs={
                    'required': True,
                    'placeholder': '-',
                    'class': 'custom-input'
                }
            ),
            'propuesta_3': forms.Select(
                attrs={
                    'required': True,
                    'placeholder': '-',
                    'class': 'custom-input'
                }
            ),
            'propuesta_4': forms.Select(
                attrs={
                    'required': True,
                    'placeholder': '-',
                    'class': 'custom-input'
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        opciones = [(i, str(i)) for i in range(1, 5)]  # Generar opciones del 1 al 4
        for i in range(1, 5):
            self.fields[f'propuesta_{i}'].widget = forms.Select(choices=opciones)

    def clean(self):
        cleaned_data = super().clean()

        # Validar que todos los campos estén llenos
        for i in range(1, 5):
            propuesta = cleaned_data.get(f'propuesta_{i}')
            if not propuesta:
                self.add_error(f'propuesta_{i}', 'Debes evaluar este enunciado antes de continuar.')

        # Validar que los valores sean distintos
        valores = [
            cleaned_data.get('propuesta_1'),
            cleaned_data.get('propuesta_2'),
            cleaned_data.get('propuesta_3'),
            cleaned_data.get('propuesta_4'),
        ]
        if len(valores) != len(set(valores)):
            self.add_error(None, 'Cada afirmación debe tener una valoración distinta.')

        return cleaned_data


class PreguntaCincoForm(forms.ModelForm):
    class Meta:
        model = PreguntaCinco
        fields = ['texto_respuesta']

        widgets = {
            'texto_respuesta': forms.Textarea(attrs={'required': False, 'placeholder': 'Escribe aquí tu respuesta.'})
        }
