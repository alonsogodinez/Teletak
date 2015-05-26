# -*- encoding: utf-8 -*-
from django import forms
from .models import User


class LoginForm(forms.ModelForm):

    username = forms.CharField(widget= forms.TextInput(attrs={'class':'login-input  form-control '}),label= "Usuario")

    password = forms.CharField(widget= forms.PasswordInput(attrs={'class':'login-input form-control '}),label= "Contraseña")


    class Meta:
        model = User
        fields = ['username', 'password']