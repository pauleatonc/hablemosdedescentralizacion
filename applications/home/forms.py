from django import forms
from .models import Contact
from captcha.fields import ReCaptchaField


class ContactForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['message'].widget.attrs.update({'oninput': 'countWords()'})

    class Meta:
        model = Contact
        fields = ('full_name', 'email', 'contact_reason', 'message')

        labels = {
            'full_name': 'Nombre completo (obligatorio)',
            'email': 'Correo electrónico institucional (obligatorio)',
            'contact_reason': 'Razón de contacto (obligatorio)',
            'message': 'Comentario (obligatorio)'
        }

        widgets = {
            'full_name': forms.TextInput(attrs={'required': True, 'placeholder': 'Ingresa tu nombre.', 'class': 'custom-input'}),
            'email': forms.EmailInput(attrs={'required': True, 'placeholder': 'Ingresa tu correo electrónico.', 'class': 'custom-input'}),
            'contact_reason': forms.Select(attrs={'required': True, 'placeholder': 'Elige una opción', 'class': 'custom-select'}),
            'message': forms.Textarea(attrs={'required': True, 'placeholder': 'Describe la razón de contacto.', 'class': 'custom-textarea'}),
        }

    captcha = ReCaptchaField()

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email and '@' not in email:
            raise forms.ValidationError('Por favor, introduce un correo electrónico válido.')
        return email

    def clean_message(self):
        message = self.cleaned_data.get('message')
        word_limit = 250  # Número máximo de palabras permitidas

        if message:
            word_count = len(message.split())
            if word_count > word_limit:
                raise forms.ValidationError(f'El comentario no puede exceder {word_limit} palabras.')
        return message
