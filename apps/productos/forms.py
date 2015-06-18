__author__ = 'kevin'

from django import forms
from apps.almacen.models import Producto

class RegistrarProductoForm(forms.ModelForm):
    codigo = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class': 'form-control'}), label="Codigo")
    sap = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control '}), label="SAP")
    descripcion = forms.EmailField(max_length=30, widget=forms.EmailInput(attrs={'class': 'form-control'}),
                                   label="Descripcion")
    categoria = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control '}),
                                label="Categoria")




