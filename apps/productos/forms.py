__author__ = 'kevin'

from django import forms
from apps.almacen.models import Producto

class RegistrarProductoForm(forms.ModelForm):
    codigo = forms.CharField(max_length=10, widget=forms.TextInput(attrs={'class': 'form-control'}), label="Codigo")
    sap = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class': 'form-control '}), label="SAP")
    descripcion = forms.EmailField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}),
                                   label="Descripcion")
    categoria = forms.CharField(max_length=10, widget=forms.TextInput(attrs={'class': 'form-control '}),
                                label="Categoria")




