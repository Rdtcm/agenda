# flake8: noqa
from django import forms
from django.core.exceptions import ValidationError
from . import models
from  django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User


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


class RegisterForm(UserCreationForm):

    first_name = forms.CharField(
        required=True
    )

    last_name = forms.CharField(
        required=True
    )

    email = forms.CharField(
        required=True
    )

    class Meta:
        model = User
        fields = (
            'first_name', 'last_name', 'email',
            'username', 'password1', 'password2',
        )
    
    def clean_email(self):
        email = self.cleaned_data.get('email')

        if User.objects.filter(email=email).exists():
            self.add_error(
                'email',
                ValidationError('Um usuario ja possui este email', code='invalid')
            )

        return email