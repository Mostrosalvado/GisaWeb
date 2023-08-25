from django import forms
from django.core import validators
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User

class ContactForm(forms.Form):
    name = forms.CharField(max_length=255, label='Nombre')
    email = forms.EmailField(label='Correo electrónico')
    message = forms.CharField(widget=forms.Textarea, label='Mensaje')
    
    verbose_name = 'Formulario de contacto'
    verbose_name_plural = 'Formularios de contacto'


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','first_name','last_name','password1','password2']
        verbose_name = 'ModelName'
        verbose_name_plural = 'ModelNames'