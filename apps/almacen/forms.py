# coding=utf-8
from datetime import date
from django import forms
from django.forms.models import inlineformset_factory
from django.utils import timezone
from .models import GuiaRemision,Ingreso,DetalleIngreso,Proveedor
from apps.productos.models import Producto,UnidadMedicion
from apps.usuarios.forms import User
from .models import Almacen

class UsuarioForm(forms.ModelForm):
    dni = forms.ModelChoiceField(queryset=User.objects.all(),widget=forms.Select(attrs={'class':'form-control'}),
                                 label="Unidad de Medida")
    class Meta:
        model=User
        fields = ('dni',)

class IngresoForm(forms.ModelForm):
    almacen = forms.ModelChoiceField(queryset=Almacen.objects.all(),
                                     widget=forms.Select(attrs={'class':'form-control chosen-select',
                                                                'placeholder':'almacen'}),
                                     label= 'Almacen')

    class Meta:
        model = Ingreso
        fields = ('tipo','dni_usuario','almacen')

class DetalleIngresoForm(forms.ModelForm):
    # serie = forms.CharField(max_length=10,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Serie'}),
    #                         label="Serie")
    cantidad = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'Cantidad'}),
                                  label="Cantidad")
    unidad_caja = forms.ModelChoiceField(queryset=UnidadMedicion.objects.all(),
                                         widget=forms.Select(attrs={'class':'form-control chosen-select',
                                                                    'placeholder':'Unidad de medida'}),
                                         label="Unidad de medida")
    estado = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Estado'}),
                             label="Estado del producto")
    codigo_producto = forms.ModelChoiceField(queryset=Producto.objects.all(),
                                          widget=forms.Select(attrs={'class':'form-control chosen-select',
                                                                     'placeholder':'Codigo'}))
    class Meta:
        model = DetalleIngreso
        fields = ('cantidad','unidad_caja','estado','codigo_producto','id_almacen')

DetalleIngresoFormSet = inlineformset_factory(Ingreso,DetalleIngreso,extra=1,can_delete=False, form=DetalleIngresoForm)

class ProductoForm(forms.ModelForm):
    codigo_product = forms.ModelChoiceField(queryset=Producto.objects.all(),
                                            widget=forms.Select(attrs={'class':'form-control'}),
                                            label="Unidad de Medida")
    class Meta:
        model = Producto
        fields = ('codigo',)

class GuiaRemisionForm(forms.ModelForm):
    fecha_traslado = forms.DateField(initial=timezone.now().strftime('%Y-%m-%d'),
                                     widget= forms.DateInput(attrs={'class':'form-control','type':'date'}),
                                     label="Fecha de traslado")
    punto_partida = forms.CharField(max_length=10,
                                    widget=forms.TextInput(attrs={'class':'form-control',
                                                                  'placeholder':'punto de partida'}),
                                    label="Punto de partida")
    nro_guia_remitente = forms.CharField(max_length=10,
                                         widget=forms.TextInput(attrs={'class':'form-control',
                                                                       'placeholder':'nº guia remitente'}),
                                         label="Guia remitente")
    placa_vehiculo = forms.CharField(max_length=10,
                                     widget=forms.TextInput(attrs={'class':'form-control',
                                                                   'placeholder':'placa de vehiculo'}),
                                     label="Placa de vehiculo")
    licencia_conducir = forms.CharField(max_length=10,
                                        widget=forms.TextInput(attrs={'class':'form-control',
                                                                      'placeholder':'licencia de conducir'}),
                                        label="Licencia de conducir")
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


