from django import forms
from django.core.exceptions import ValidationError
import random
from collections import OrderedDict

from .models import PreguntaUno, PreguntaDos, PreguntaTres, PreguntaCuatro, PreguntaCinco
from applications.users.models import User
from applications.regioncomuna.models import Comuna, Region
from django.utils.safestring import mark_safe


class DatosUsuarioForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('comuna', 'genero', 'edad', 'politica_privacidad')
        labels = {
            'comuna': '¿En qué comuna vives?',
            'genero': '¿Con qué género te identificas?',
            'edad': '¿Qué edad tienes?',
            'politica_privacidad': 'Leí y acepto la Política de Privacidad.'
        }
        widgets = {
            'comuna': forms.Select(
                attrs={
                    'required': True,
                    'id': 'id_comuna',
                    'placeholder': 'Ingresa una opción',
                    'class': 'form-control border border-2 border-accent rounded text-muted',
                }
            ),
            'genero': forms.Select(
                attrs={
                    'required': True,
                    'placeholder': "Elige una opción",
                    'class': 'form-control border border-2 border-accent rounded text-muted',
                    'style': 'font-level-5',
                }
            ),
            'edad': forms.NumberInput(
                attrs={
                    'required': True,
                    'placeholder': 'Ingresa tu edad',
                    'class': 'form-control border border-2 border-accent rounded text-muted'
                }
            ),
            'politica_privacidad': forms.CheckboxInput(
                attrs={
                    'required': True,
                    'class': ' custom-control custom-checkbox',
                    'style':'width:20px ; margin: 0px 8px 8px 0px ',
                }
            ),
        }

    def clean(self):
        cleaned_data = super().clean()

        comuna = cleaned_data.get('comuna')
        genero = cleaned_data.get('genero')
        edad = cleaned_data.get('edad')
        politica_privacidad = cleaned_data.get('politica_privacidad')

        if not comuna:
            self.add_error(
                'comuna', 'Debes elegir una comuna antes de continuar.')

        if not genero:
            self.add_error(
                'genero', 'Debes seleccionar un género antes de continuar.')

        if not edad:
            self.add_error(
                'edad', 'Debes introducir tu edad antes de continuar.')

        if not politica_privacidad:
            self.add_error(
                'politica_privacidad', 'Debes aceptar la Política de Privacidad antes de continuar.')

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
            raise ValidationError(
                'Debes elegir una opción antes de continuar.')
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
                    'class': 'propuesta ',
                    'id': 'propuesta_1'
                }
            ),
            'propuesta_2': forms.NumberInput(
                attrs={
                    'required': True,
                    'placeholder': '-',
                    'class': 'propuesta ',
                    'id': 'propuesta_2'
                }
            ),
            'propuesta_3': forms.NumberInput(
                attrs={
                    'required': True,
                    'placeholder': '-',
                    'class': 'propuesta ',
                    'id': 'propuesta_3'
                }
            ),
            'propuesta_4': forms.NumberInput(
                attrs={
                    'required': True,
                    'placeholder': '-',
                    'class': 'propuesta  ',
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
    
    def __init__(self, *args, **kwargs):
        request = kwargs.pop('request', None)
        super(PreguntaDosForm, self).__init__(*args, **kwargs)

        propuestas = ['propuesta_1', 'propuesta_2', 'propuesta_3', 'propuesta_4']
        if 'propuestas_order' in request.session:
            propuestas_order = request.session['propuestas_order']
            self.fields = OrderedDict((k, self.fields[k]) for k in propuestas_order)
        else:
            random.shuffle(propuestas)
            request.session['propuestas_order'] = propuestas
            self.fields = OrderedDict((k, self.fields[k]) for k in propuestas)
            
    
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
    
    def __init__(self, *args, **kwargs):
        request = kwargs.pop('request', None)
        super(PreguntaTresForm, self).__init__(*args, **kwargs)

        iniciativas = ['iniciativa_1', 'iniciativa_2', 'iniciativa_3', 'iniciativa_4', 'iniciativa_5']
        if 'iniciativas_order' in request.session:
            iniciativas_order = request.session['iniciativas_order']
            self.fields = OrderedDict((k, self.fields[k]) for k in iniciativas_order)
        else:
            random.shuffle(iniciativas)
            request.session['iniciativas_order'] = iniciativas
            self.fields = OrderedDict((k, self.fields[k]) for k in iniciativas)
    

class PreguntaCuatroForm(forms.ModelForm):
    class Meta:
        model = PreguntaCuatro
        fields = ('tematica_1', 'tematica_2', 'tematica_3', 'tematica_4', 'tematica_5') 
        widgets = {
            'tematica_1': forms.Select(
                attrs={
                    'required': True,
                    'class': 'form-control w-50 border border-2 border-gray-a align-self-center mx-auto'
                } 
            ),
            'tematica_2': forms.Select(
                attrs={
                    'required': True,
                    'class': 'form-control w-50 border border-2 border-gray-a align-self-center mx-auto'
                }
            ),
            'tematica_3': forms.Select(
                attrs={
                    'required': True,              
                    'class': 'form-control w-50 border border-2 border-gray-a align-self-center mx-auto'
                }
            ),
            'tematica_4': forms.Select(
                attrs={
                    'required': True,
                    'class': 'form-control w-50 border border-2 border-gray-a align-self-center mx-auto'
                }
            ),
            'tematica_5': forms.Select(
                attrs={
                    'required': True,
                    'class': 'form-control w-50 border border-2 border-gray-a align-self-center mx-auto'
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        request = kwargs.pop('request', None)
        super(PreguntaCuatroForm, self).__init__(*args, **kwargs)

        tematicas = ['tematica_1', 'tematica_2', 'tematica_3', 'tematica_4', 'tematica_5']
        if 'tematicas_order' in request.session:
            tematicas_order = request.session['tematicas_order']
            self.fields = OrderedDict((k, self.fields[k]) for k in tematicas_order)
        else:
            random.shuffle(tematicas)
            request.session['tematicas_order'] = tematicas
            self.fields = OrderedDict((k, self.fields[k]) for k in tematicas)

        for field in self.fields:
            self.fields[field].label = mark_safe('<span style="font-weight: 700; ; text-decoration-line: underline;">' + self.fields[field].label + '</span>: ' + self.fields[field].help_text)

        # Reemplazar la opción "---------" por "Elige una opción"
        for field_name, field in self.fields.items():
            field.choices = [('', 'Elige una opción')] + list(field.choices)[1:]


class PreguntaCincoForm(forms.ModelForm):
    class Meta:
        model = PreguntaCinco
        fields = ['texto_respuesta']
        label = 'Escribe tu respuesta'

        widgets = {
            'texto_respuesta': forms.Textarea(attrs={'required': False, 'placeholder': 'Escribe aquí tu respuesta.','class': 'form-control'})
        }


class EnviarFormulariosForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'recibir_resultados']

        labels = {
            'email': 'Correo electrónico (obligatorio)',
            'recibir_resultados': 'También quiero recibir los resultados finales del proceso.'
        }

        widgets = {
            'email': forms.EmailInput(
                attrs={
                    'required': True,
                    'placeholder': 'ejemplo@ejemplo.cl',
                    'class': 'custom-input'
                }
            ),
            'recibir_resultados': forms.CheckboxInput(
                attrs={
                    'required': False,
                    'class': ' custom-control custom-checkbox',
                    'style': 'width:20px ; margin: 0px 8px 8px 0px ',
                }
            ),
        }
