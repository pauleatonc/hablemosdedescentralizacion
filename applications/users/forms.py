from django import forms
from django.contrib.auth import authenticate

from .functions import validar_rut_form


class LoginForm(forms.Form):
    rut = forms.CharField(
        label='Rut',
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Ingresa tu RUT',
                'class': 'custom-input'
            }
        )
    )

    password = forms.CharField(
        label='Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Ingresa tu contraseña',
                'class': 'custom-input'
            }
        )
    )

    def clean_rut(self):
        """
        Realiza la validación y el formateo del campo Rut
        """
        rut = validar_rut_form(self)
        return rut

    def clean(self):
        """
        Realiza la validación y la autenticación del formulario en su conjunto
        """
        cleaned_data = super().clean()
        rut = cleaned_data.get('rut')
        password = cleaned_data.get('password')
        if rut and password:
            user = authenticate(username=rut, password=password)
            if user is None:
                self.add_error('password', 'Usuario y/o contraseña incorrectos')
        return cleaned_data