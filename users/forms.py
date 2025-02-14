from tabnanny import verbose

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True, label='Email', widget=forms.EmailInput(attrs={'class': 'registration__input'}))
    password1 = forms.CharField(required=True, label='Password', widget=forms.PasswordInput(attrs={'class': 'registration__input'}))
    password2 = forms.CharField(required=True, label='Repeat Password', widget=forms.PasswordInput(attrs={'class': 'registration__input'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        labels = {
            'username': 'Login',
        }
        widgets = {
            'username': forms.TextInput(attrs={'class': 'registration__input'}),
        }
