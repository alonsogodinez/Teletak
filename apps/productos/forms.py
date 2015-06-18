from django import forms
from django.forms import ModelForm
from apps.almacen.models import Producto,Categoria

class ProductoForm(forms.ModelForm):
    sap = forms.CharField(max_length=10,widget=forms.TextInput(attrs={'class':'form-control'}),label="SAP")
    descripcion = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class':'form-control'}),label="Descripcion")
    categoria = forms.ModelChoiceField(queryset=Categoria.objects.all(),widget=forms.Select(attrs={'class':'form-control'}),label="Categoria")
    stock_minimo = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}),label="Stock Minimo")
    class Meta:
        model = Producto
        fields = ('sap','descripcion','categoria','stock_minimo',)
