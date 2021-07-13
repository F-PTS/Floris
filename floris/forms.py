from django import forms
from django.forms.fields import CharField


class LoginForm(forms.Form):
    login = forms.CharField(label='Login', max_length=64)
    password = forms.CharField(widget=forms.PasswordInput())

class RegisterForm(forms.Form):
    login = forms.CharField(label='Login', max_length=64)
    mail = forms.CharField(label='Email', max_length=64)
    password = forms.CharField(widget=forms.PasswordInput())
    repeated_password = forms.CharField(label='Repeat password',widget=forms.PasswordInput())

class PlantForm(forms.Form):
    name = forms.CharField(label='Nazwa twojego kwiatka', max_length=64)
    water_time = forms.IntegerField(label='Co ile chcesz go podlewac')
