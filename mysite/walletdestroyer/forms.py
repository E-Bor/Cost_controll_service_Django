from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from .models import SpendingCategoriesModel


class EarningsForm(forms.Form):
    time_create = forms.DateField(
        required=True,
        label='Дата',
        widget=forms.DateInput(
            attrs={
                'name': 'time_create',
                'type': 'date',
                'class': 'form-control',
                'placeholder': 'date',
            }))
    cost = forms.CharField(
        required=True,
        label='Заработок',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )


class SpendingForm(forms.Form):

    DEFAULT_CATEGORY_VALUE = 'Выберите категорию'

    CATEGORY_CHOICES = (
                ('', DEFAULT_CATEGORY_VALUE),
                *SpendingCategoriesModel.get_all_categories()
            )

    time_create = forms.DateField(
        required=True,
        label='Дата',
        widget=forms.DateInput(
            attrs={
                'name': 'time_create',
                'type': 'date',
                'class': 'form-control',
                'placeholder': 'date',
            }))

    description = forms.CharField(
        label='Описание',
        required=False,
        widget=forms.Textarea(
            attrs={
                'name': 'description',
                'class': 'form-control',
                'placeholder': 'Укажите на что вы потратили деньги',
                'rows': 3,

            }
        ),

    )

    category = forms.ChoiceField(
        label='Категория',
        required=True,
        widget=forms.Select(
            attrs={
                'class': 'form-select',
            },
        ),
        choices=CATEGORY_CHOICES,
    )
    cost = forms.CharField(
        required=True,
        label='Цена',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'
            }
        )
    )


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