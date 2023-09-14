from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class EarningsForm(forms.Form):
    date = forms.DateTimeField(required=True, label='Дата')
    cost = forms.CharField(label='Заработок')


class SpendingForm(forms.Form):
    date = forms.DateTimeField(required=True, label='Дата')
    cost = forms.CharField(label='Цена')
    category = forms.CharField(label='Категория')
    description = forms.CharField(label='Описание')


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')


class AuthUserForm(AuthenticationForm):
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))