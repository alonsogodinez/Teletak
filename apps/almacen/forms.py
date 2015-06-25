from django import forms

from .models import GuiaRemision,Ingreso,DetalleIngreso

class EntradaForm(forms.ModelForm):

    dni_usuario = forms.CharField(max_length=8,widget=forms.TextInput(attrs={'class':'form-control'}),label="DNI")
    fecha       = forms.DateField()
    sap = forms.CharField(max_length=10,widget=forms.TextInput(attrs={'class':'form-control'}),label="SAP")
    descripcion = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class':'form-control'}),label="Descripcion")
    categoria = forms.ModelChoiceField(queryset=Categoria.objects.all(),widget=forms.Select(attrs={'class':'form-control'}),label="Categoria")
    stock_minimo = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}),label="Stock Minimo")
    class Meta:
        model = GuiaRemision
        fields = ('sap','descripcion','categoria','stock_minimo',)

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre',]