from django import forms
from django.core import validators


class ContactForm(forms.Form):
    name = forms.CharField(label='Nombre', widget=forms.TextInput({
        'class': 'form-control',
        'placeholder': 'Nombre Completo'
    }),required=True, min_length=20)

    email = forms.EmailField(label='Correo', widget=forms.EmailInput({
        'class': 'form-control',
        'placeholder': 'example@email.com'
    }), required=True)

    number = forms.CharField(label='Telefono', widget=forms.TextInput({
        'class': 'form-control',
        'placeholder': '5555 5555'
    }), required=True)

    business = forms.CharField(label='Empresa', widget=forms.TextInput({
        'class': 'form-control',
        'placeholder': 'Empresa'
    }), required=True)

    city = forms.CharField(label='Ciudad', widget=forms.TextInput({
        'class': 'form-control',
        'placeholder': 'Ciudad'
    }), required=True)
    
    country = forms.CharField(label='Pais', widget=forms.TextInput({
        'class': 'form-control',
        'placeholder': 'Pais'
    }), required=True)

    message = forms.CharField(label='Mensaje', widget=forms.Textarea({
        'class': 'form-control',
        'placeholder': 'Escribe tu mensaje...',
        'rows': 4
    }), required=True)
