# coding=utf-8
from django import forms
from django.forms import ModelForm, formset_factory
from .models import Producto,Categoria,UnidadMedicion,ProductoMedida

class ProductoForm(forms.ModelForm):
    sap = forms.ModelChoiceField(queryset=Producto.objects.all(),widget=forms.Select(attrs={'class':'form-control'}),label="Unidad de Medida")
    descripcion = forms.CharField(max_length=50,
                                  widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Descripción'}),
                                  label="Descripcion")
    categoria = forms.ModelChoiceField(queryset=Categoria.objects.all(),
                                       widget=forms.Select(attrs={'class':'form-control','placeholder':'Categoría'}),
                                       label="Categoria")
    stock_minimo = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control',
                                                                      'placeholder':'Stock mínimo'}),
                                      label="Stock Minimo")

    class Meta:
        model = Producto
        fields = ('sap','descripcion','categoria','stock_minimo',)

class UnidadProductoForm(forms.ModelForm):
    id_unidad = forms.ModelChoiceField(queryset=UnidadMedicion.objects.all(),
                                       widget=forms.Select(attrs={'class':'form-control'}),
                                       label="Equivalencia")
    equivalencia = forms.DecimalField(max_digits=4,decimal_places=2,
                                      widget=forms.NumberInput(attrs={'class':'form-control',
                                                                      'placeholder':'Equivalencia'}),
                                      label="Equivalencia")
    class Meta:
        model = ProductoMedida
        fields = ['id_unidad','equivalencia',]

UnidadProductoFormSet = formset_factory(UnidadProductoForm, extra=1, max_num=10)

class CategoriaForm(forms.ModelForm):
    nombre = forms.CharField(max_length=15,widget=forms.TextInput(attrs={'class':'form-control'}),label="Nombre")
    class Meta:
        model = Categoria
        fields = ['nombre',]