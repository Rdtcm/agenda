# flake8: noqa
from django import forms
from django.core.exceptions import ValidationError
from . import models


class ContactForm(forms.ModelForm):
    picture = forms.ImageField(
        widget=forms.FileInput(
            attrs={
                'accept': 'image/*',
            }
        )
    )
    
    class Meta:
        model = models.Contact
        fields = (
            'first_name', 'last_name', 'phone', 'email', 
            'description', 'category', 'picture'
        )
    
    # Metodo para validacoes do formulario
    def clean(self):
        cleaned_data = self.cleaned_data
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')
        email = cleaned_data.get('email')

        if first_name == last_name:
            mensagem = ValidationError(
                'O primeiro nome nao pode ser igual ao segundo!',
                code='invalid'
            )
            self.add_error('first_name', mensagem)
            self.add_error('last_name', mensagem)
            self.add_error('email', ValidationError('E-mail Invalido', code='invalid'))

        return super().clean()

    