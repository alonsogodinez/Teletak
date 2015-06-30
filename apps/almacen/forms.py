from datetime import date
from django import forms

from .models import GuiaRemision,Ingreso,DetalleIngreso,Proveedor,Salida,DetalleSalida
from apps.productos.models import Producto
from apps.usuarios.forms import User

class UsuarioForm(forms.ModelForm):
    dni = forms.ModelChoiceField(queryset=User.objects.all(),widget=forms.Select(attrs={'class':'form-control'}),label="Unidad de Medida")
    class Meta:
        model=User
        fields = ('dni',)

class IngresoForm(forms.ModelForm):
    dni_usuario = forms.CharField(max_length=8,widget=forms.TextInput(attrs={'class':'form-control'}),label="DNI")
    fecha       = forms.DateField(initial=date.today(),widget= forms.DateInput(attrs={'class':'form-control'}),label="Fecha")
    class Meta:
        model = Ingreso
        fields = ('dni_usuario','fecha',)

class DetalleIngresoForm(forms.ModelForm):
    serie = forms.CharField(max_length=10,widget=forms.TextInput(attrs={'class':'form-control'}),label="Punto de partida")
    cantidad = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}),label="Cantidad")
    unidad_caja = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}),label="Unidad de caja")
    estado = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}),label="Estado")
    class Meta:
        model = DetalleIngreso
        fields = ('serie','cantidad','unidad_caja','estado',)

class ProductoForm(forms.ModelForm):
    codigo_product = forms.ModelChoiceField(queryset=Producto.objects.all(),widget=forms.Select(attrs={'class':'form-control'}),label="Unidad de Medida")
    class Meta:
        model = Producto
        fields = ('codigo',)

class GuiaRemisionForm(forms.ModelForm):
    fecha_traslado = forms.DateField(initial=date.today(),widget= forms.DateInput(attrs={'class':'form-control'}),label="Fecha")
    punto_partida = forms.CharField(max_length=10,widget=forms.TextInput(attrs={'class':'form-control'}),label="Punto de partida")
    nro_guia_remitente = forms.CharField(max_length=10,widget=forms.TextInput(attrs={'class':'form-control'}),label="Guia remitente")
    placa_vehiculo = forms.CharField(max_length=10,widget=forms.TextInput(attrs={'class':'form-control'}),label="Placa de vehiculo")
    licencia_conducir = forms.CharField(max_length=10,widget=forms.TextInput(attrs={'class':'form-control'}),label="Licencia de conducir")
    class Meta:
        model= GuiaRemision
        fields = ('fecha_traslado','punto_partida','nro_guia_remitente','placa_vehiculo','licencia_conducir',)


class ProveedoresForm(forms.ModelForm):
    ruc = forms.CharField(max_length=10,widget=forms.TextInput(attrs={'class':'form-control'}),label="RUC")
    nombre = forms.CharField(max_length=10,widget=forms.TextInput(attrs={'class':'form-control'}),label="Nombre")
    direccion = forms.CharField(max_length=10,widget=forms.TextInput(attrs={'class':'form-control'}),label="Direccion")

    class Meta:
        model = Proveedor
        fields = ('ruc','nombre','direccion',)

#SALIDAS

class SalidaForm(forms.ModelForm):
    id_almacen = forms.ModelChoiceField(queryset=Almacen.objects.all(),widget=forms.Select(attrs={'class':'form-control'}),label="Almacen")
    dni_usuario = forms.ModelChoiceField(queryset=User.objects.all(),widget=forms.Select(attrs={'class':'form-control'}),label="Usuario")
    nodo = forms.CharField(max_length=15,widget=forms.TextInput(attrs={'class':'form-control'}),label="Nodo de Trabajo")
    devolucion = forms.BooleanField(initial=True,widget=forms.CheckboxInput(),label="Retirar productos para devolver al proveedor")
    class Meta:
        model = Salida
        fields = ('id_almacen','dni_usuario','nodo','devolucion',)

class DetalleSalidaForm(forms.ModelForm):
    codigo_producto = forms.ModelChoiceField(queryset=Producto.objects.all(),widget=forms.Select(attrs={'class':'form-control'}),label="Producto")
    cantidad = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}),label="Cantidad")
    class Meta:
        model = DetalleSalida
        fields = ('codigo_producto','cantidad',)
