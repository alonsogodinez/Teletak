from django.forms.models import inlineformset_factory, formset_factory
from django import forms
from .models import GuiaRemision,Ingreso,DetalleIngreso,Proveedor,Salida,DetalleSalida,Almacen
from django.utils import timezone
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
                                                                'placeholder':'almacen','required':True}),
                                     label= 'Almacen')

    class Meta:
        model = Ingreso
        fields = ('tipo','dni_usuario','almacen')

class DetalleIngresoForm(forms.ModelForm):
    # serie = forms.CharField(max_length=10,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Serie'}),
    #                         label="Serie")
    cantidad = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control',
                                                                  'placeholder':'Cantidad',
                                                                  'required':True}),
                                  label="Cantidad")
    unidad_caja = forms.ModelChoiceField(queryset=UnidadMedicion.objects.all(),
                                         widget=forms.Select(attrs={'class':'form-control chosen-select',
                                                                    'required':True,
                                                                    'placeholder':'Unidad de medida'}),
                                                            label="Unidad de medida")
    estado = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control',
                                                           'placeholder':'Estado',
                                                           'required':True}),
                                                    label="Estado del producto")
    codigo_producto = forms.ModelChoiceField(queryset=Producto.objects.all(),
                                            widget=forms.Select(attrs={'class':'form-control chosen-select',
                                                                     'placeholder':'Codigo',
                                                                     'required':True}))
    class Meta:
        model = DetalleIngreso
        fields = ('cantidad','unidad_caja','estado','codigo_producto',)

DetalleIngresoFormSet = inlineformset_factory(Ingreso,DetalleIngreso,extra=1,can_delete=False, form=DetalleIngresoForm)

class ProductoForm(forms.ModelForm):
    codigo_product = forms.ModelChoiceField(queryset=Producto.objects.all(),
                                            widget=forms.Select(attrs={'class':'form-control',
                                                                       'required':True}),
                                            label="Unidad de Medida")
    class Meta:
        model = Producto
        fields = ('codigo',)

class GuiaRemisionForm(forms.ModelForm):
    fecha_traslado = forms.DateField(initial=timezone.now().strftime('%Y-%m-%d'),
                                     widget= forms.DateInput(attrs={'class':'form-control',
                                                                    'type':'date',
                                                                    'required':True}),
                                     label="Fecha de traslado")
    punto_partida = forms.CharField(max_length=10,
                                    widget=forms.TextInput(attrs={'class':'form-control',
                                                                  'placeholder':'Punto de partida',
                                                                  'required':True}),
                                    label="Punto de partida")
    nro_guia_remitente = forms.CharField(max_length=10,
                                         widget=forms.TextInput(attrs={'class':'form-control',
                                                                       'placeholder':'N| guia remitente',
                                                                       'required':True}),
                                         label="Guia remitente")
    placa_vehiculo = forms.CharField(max_length=10,
                                     widget=forms.TextInput(attrs={'class':'form-control',
                                                                   'placeholder':'Placa de vehiculo',
                                                                   'required':True}),
                                     label="Placa de vehiculo")
    licencia_conducir = forms.CharField(max_length=10,
                                        widget=forms.TextInput(attrs={'class':'form-control',
                                                                      'placeholder':'Licencia de conducir',
                                                                      'required':True}),
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

DetalleIngresoFormSet = inlineformset_factory(Ingreso,DetalleIngreso,
                                              can_delete=False,
                                              extra=2,
                                             max_num=3,
                                              form=DetalleIngresoForm)

#SALIDAS

class SalidaForm(forms.ModelForm):
    dni_usuario = forms.ModelChoiceField(queryset=User.objects.all(),widget=forms.Select(attrs={'class':'form-control','required':'true'}),label="Usuario")
    nodo = forms.CharField(max_length=15,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Nombre del Nodo'}),label="Nodo de Trabajo",required=False)
    devolucion = forms.BooleanField(initial=False,widget=forms.CheckboxInput(),label="Devolver productos defectuosos al proveedor",required=False)
    class Meta:
        model = Salida
        fields = ('dni_usuario','nodo','devolucion',)

class DetalleSalidaForm(forms.ModelForm):
    id_almacen = forms.ModelChoiceField(queryset=Almacen.objects.all(),widget=forms.Select(attrs={'class':'form-control c-almacen','required':'true',}),label="Almacen")
    codigo_producto = forms.ModelChoiceField(Producto.objects,widget=forms.Select(attrs={'class':'form-control c-producto','disabled': 'true'}))
    cantidad = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control','disabled': 'true','min':'0'}),label="Cantidad")
    class Meta:
        model = DetalleSalida
        fields = ('id_almacen','codigo_producto','cantidad',)

DetalleSalidaFormset = inlineformset_factory(Salida,DetalleSalida,extra=1,can_delete=True,form=DetalleSalidaForm)