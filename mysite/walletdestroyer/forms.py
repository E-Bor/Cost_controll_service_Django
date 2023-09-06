from django import forms


class EarningsForm(forms.Form):
    date = forms.DateTimeField(required=True, label='Дата')
    cost = forms.CharField(label='Заработок')


class SpendingForm(forms.Form):
    date = forms.DateTimeField(required=True, label='Дата')
    cost = forms.CharField(label='Цена')
    category = forms.CharField(label='Категория')
    description = forms.CharField(label='Описание')