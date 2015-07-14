from django.db import models
from apps.usuarios.models import User
from apps.productos.models import Producto, UnidadMedicion
from django.utils import timezone


class Proveedor(models.Model):
    ruc = models.CharField(max_length=10,primary_key=True)
    nombre = models.CharField(max_length=30)
    direccion = models.CharField(max_length=30)

    class Meta:
        verbose_name_plural = "Proveedores"

    def __unicode__(self):
        return self.nombre

class GuiaRemision(models.Model):
    fecha_traslado = models.DateField()
    punto_partida = models.CharField(max_length=30)
    nro_guia_remitente = models.CharField(max_length=15)
    placa_vehiculo = models.CharField(max_length=10)
    licencia_conducir = models.CharField(max_length=15)
    proveedor = models.ForeignKey(Proveedor,blank=True,null=True)

    class Meta:
        verbose_name_plural = "Guias de remision"

    def __unicode__(self):
        return self.nro_guia_remitente

class Ingreso(models.Model):
    dni_usuario = models.ForeignKey(User, blank=True, null=True)
    fecha = models.DateField(default=timezone.now ,blank=True, null=True)
    guia_remision = models.ForeignKey(GuiaRemision, blank=True, null=True)
    tipo = models.IntegerField(blank=True, null=True) #ingreso :1   , reingreso:2

    def __unicode__(self):
        return  self.guia_remision.nro_guia_remitente + ' ' +  self.fecha.strftime('%Y/%m/%d')

class Almacen(models.Model):
    ubicacion = models.CharField(max_length=50, blank=True, null=True)
    capacidad = models.IntegerField(blank=True,null=True)

    class Meta:
        verbose_name_plural = "Almacenes"

    def __unicode__(self):
        return self.ubicacion


class DetalleIngreso(models.Model):
    codigo_producto = models.ForeignKey(Producto, blank=True, null=True)
    id_almacen = models.ForeignKey(Almacen,blank=True,null=True)
    id_ingreso = models.ForeignKey(Ingreso, blank=True, null=True)
    cantidad = models.IntegerField(blank=True,null=True)
    estado = models.CharField(max_length=10, blank=True, null=True)

    def __unicode__(self):
        return 'asdfa'


class Salida(models.Model):
    dni_usuario = models.ForeignKey(User,blank=True,null=True)
    id_almacen = models.ForeignKey(Almacen,blank=True,null=True)
    fecha = models.DateField(blank=True, null=True)
    nodo = models.CharField(max_length=15, blank=True, null=True)
    devolucion = models.NullBooleanField()

    def __unicode__(self):
        return self.fecha.strftime('%Y/%m/%d')+' ' + nodo

class DetalleSalida(models.Model):
    codigo_producto = models.ForeignKey(Producto, blank=True, null=True)
    id_salida = models.ForeignKey(Salida, blank=True, null=True)
    cantidad = models.IntegerField(blank=True, null=True)

    def __unicode__(self):
        return self.codigo_producto.descripcion
