from django import forms
from django.core.exceptions import ValidationError

from .models import PreguntaUno, PreguntaDos, PreguntaTres, PreguntaCuatro, PreguntaCinco
from applications.users.models import User
from applications.regioncomuna.models import Comuna, Region


class DatosUsuarioForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('comuna', 'genero', 'edad')
        widgets = {
            'comuna': forms.Select(
                attrs={
                    'required': True,
                    'id': 'id_comuna',
                    'placeholder': 'Elige una opción',

                }
            ),
            'genero': forms.Select(
                attrs={
                    'required': True,
                    'placeholder': 'Elige una opción',
                }
            ),
            'edad': forms.NumberInput(
                attrs={
                    'required': True,
                    'placeholder': 'Elige una opción',
                }
            ),
        }

    def clean(self):
        cleaned_data = super().clean()

        comuna = cleaned_data.get('comuna')
        genero = cleaned_data.get('genero')
        edad = cleaned_data.get('edad')

        if not comuna:
            self.add_error('comuna', 'Debes elegir una comuna antes de continuar.')

        if not genero:
            self.add_error('genero', 'Debes seleccionar un género antes de continuar.')

        if not edad:
            self.add_error('edad', 'Debes introducir tu edad antes de continuar.')

        return cleaned_data


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
    
class PreguntaTresForm(forms.ModelForm):
    class Meta:
        model = PreguntaTres
        fields = ('iniciativa_1', 'iniciativa_2', 'iniciativa_3', 'iniciativa_4', 'iniciativa_5')
        widgets = {
            'iniciativa_1': forms.NumberInput(
                attrs={
                    'required': True,
                    'placeholder': '-',
                    'class': 'iniciativa',
                    'id': 'iniciativa_1'
                }
            ),
            'iniciativa_2': forms.NumberInput(
                attrs={
                    'required': True,
                    'placeholder': '-',
                    'class': 'iniciativa',
                    'id': 'iniciativa_2'
                }
            ),
            'iniciativa_3': forms.NumberInput(
                attrs={
                    'required': True,
                    'placeholder': '-',
                    'class': 'iniciativa',
                    'id': 'iniciativa_3'
                }
            ),
            'iniciativa_4': forms.NumberInput(
                attrs={
                    'required': True,
                    'placeholder': '-',
                    'class': 'iniciativa',
                    'id': 'iniciativa_4'
                }
            ),
            'iniciativa_5': forms.NumberInput(
                attrs={
                    'required': True,
                    'placeholder': '-',
                    'class': 'iniciativa',
                    'id': 'iniciativa_5'
                }
            ),
        }

    def clean(self):
        cleaned_data = super().clean()

        valores = [
            cleaned_data.get('iniciativa_1'),
            cleaned_data.get('iniciativa_2'),
            cleaned_data.get('iniciativa_3'),
            cleaned_data.get('iniciativa_4'),
            cleaned_data.get('iniciativa_5'),
        ]

        # Verificar que todos los campos estén presentes
        if None in valores:
            raise forms.ValidationError('Todos los campos son requeridos.')

        return cleaned_data
    

class PreguntaCuatroForm(forms.ModelForm):
    class Meta:
        model = PreguntaCuatro
        fields = ('tematica_1', 'tematica_2', 'tematica_3', 'tematica_4', 'tematica_5')
        widgets = {
            'tematica_1': forms.Select(
                attrs={
                    'required': True,
                    'placeholder': 'Elige una opción',
                    'class': 'tematica',
                }
            ),
            'tematica_2': forms.Select(
                attrs={
                    'required': True,
                    'placeholder': 'Elige una opción',
                    'class': 'tematica',
                }
            ),
            'tematica_3': forms.Select(
                attrs={
                    'required': True,
                    'placeholder': 'Elige una opción',
                    'class': 'tematica',
                }
            ),
            'tematica_4': forms.Select(
                attrs={
                    'required': True,
                    'placeholder': 'Elige una opción',
                    'class': 'tematica',
                }
            ),
            'tematica_5': forms.Select(
                attrs={
                    'required': True,
                    'placeholder': 'Elige una opción',
                    'class': 'tematica',
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        super(PreguntaCuatroForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].label = self.fields[field].label + ': ' + self.fields[field].help_text

class PreguntaCincoForm(forms.ModelForm):
    class Meta:
        model = PreguntaCinco
        fields = ['texto_respuesta']

        widgets = {
            'texto_respuesta': forms.Textarea(attrs={'required': False, 'placeholder': 'Escribe aquí tu respuesta.'})
        }
