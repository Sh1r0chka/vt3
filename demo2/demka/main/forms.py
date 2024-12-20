from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from .models import CustomUser, Ticket
from datetime import date, datetime


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=255, help_text='Обязатльное поле.')
    username = forms.EmailField(max_length=24, help_text='Обязатльное поле.')

    class Meta:
        model = CustomUser
        fields = ('username', 'phone', 'email', 'password1', 'password2')


class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Логин')
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ['username', 'password']


class NewTicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['number', 'descr']


class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['number', 'descr', 'status']