# -*- encoding: utf-8 -*-
from django import forms
from .models import User


class LoginForm(forms.ModelForm):

    username = forms.CharField(widget= forms.TextInput(attrs={'class':'form-control '}),label= "Usuario")
    password = forms.CharField(widget= forms.PasswordInput(attrs={'class':' form-control '}),label= "Contraseña")


    class Meta:
        model = User
        fields = ['username', 'password']


class RegistrarTrabajadorForm(forms.ModelForm):

    username = forms.CharField(max_length=30,
                               widget= forms.TextInput(attrs={'class':'form-control',
                                                              'placeholder':'Usuario'}),
                               label= "Usuario")

    password = forms.CharField(widget= forms.PasswordInput(attrs={'class':' form-control',
                                                                  'placeholder':'Constraseña'}),
                               label= "Contraseña")

    email = forms.EmailField(max_length=30,widget=forms.EmailInput(attrs={'class':'form-control',
                                                                          'placeholder':'Email'}),
                             label="Correo Electronico")

    first_name = forms.CharField(max_length=100,widget= forms.TextInput(attrs={'class':'form-control',
                                                                               'placeholder':'Nombres'}),
                                 label= "Nombres")

    last_name = forms.CharField(max_length=100,widget= forms.TextInput(attrs={'class':'form-control',
                                                                              'placeholder':'Apellidos'}),
                                label= "Apellidos")

    dni = forms.CharField(max_length=8,widget= forms.TextInput(attrs={'class':'form-control',
                                                                      'placeholder':'Dni'}),
                          label= "DNI")

    cellphone = forms.CharField(max_length=15, widget= forms.TextInput(attrs={'class':'form-control',
                                                                              'placeholder':'Celular'}),
                                label= "Celular")

    class Meta:
        model = User
        fields = ['username','password','email','first_name','last_name','dni','cellphone']

class EditarTrabajadorForm(forms.ModelForm):

    username = forms.CharField(max_length=30,widget= forms.TextInput(attrs={'class':'form-control','readonly':'true'}),label= "Usuario")
    email = forms.EmailField(max_length=30,widget=forms.EmailInput(attrs={'class':'form-control'}),label="Correo Electronico")
    first_name = forms.CharField(max_length=100,widget= forms.TextInput(attrs={'class':'form-control',}),label= "Nombres")
    last_name = forms.CharField(max_length=100,widget= forms.TextInput(attrs={'class':'form-control '}),label= "Apellidos")
    dni = forms.CharField(max_length=8,widget= forms.TextInput(attrs={'class':'form-control '}),label= "DNI")
    cellphone = forms.CharField(max_length=15, widget= forms.TextInput(attrs={'class':'form-control '}),label= "Celular")
    is_active = forms.BooleanField(widget= forms.CheckboxInput(attrs={'type':'checkbox'}),label= "Habilitado")
    is_staff = forms.BooleanField(widget= forms.CheckboxInput(attrs={'type':'checkbox '}),label= "Administrador",required=False)

    class Meta:
        model = User
        fields = ['username','email','first_name','last_name','dni','cellphone','is_active','is_staff']