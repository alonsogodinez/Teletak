from django.db import models
from apps.usuarios.models import User

class Categoria(models.Model):
    nombre = models.CharField(max_length=15)

class UnidadMedicion(models.Model):
    id_und = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=20)

class Producto(models.Model):
    codigo = models.AutoField(primary_key=True, max_length=10)
    sap = models.CharField(max_length=10, blank=True, null=True)
    descripcion = models.CharField(max_length=50, blank=True, null=True)
    categoria = models.ForeignKey(Categoria,blank=True,null=True)
    stock_minimo = models.IntegerField(blank=True, null=True)

class ProductoMedida(models.Model):
    unidad = models.ForeignKey(UnidadMedicion)
    prod = models.ForeignKey(Producto)
    equiv = models.DecimalField('Equivalencia',max_digits=4,decimal_places=2)

class Proveedor(models.Model):
    ruc = models.CharField(max_length=10,primary_key=True)
    nombre = models.CharField(max_length=30)
    direccion = models.CharField(max_length=30)

class GuiaRemision(models.Model):
    fecha_traslado = models.DateField()
    punto_partida = models.CharField(max_length=30)
    nro_guia_remitente = models.CharField(max_length=15)
    placa_vehiculo = models.CharField(max_length=10)
    licencia_conducir = models.CharField(max_length=15)


class Ingreso(models.Model):
    id = models.AutoField(primary_key=True)
    dni_usuario = models.ForeignKey(User, blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)
    guia_remision = models.CharField(max_length=20, blank=True, null=True)


class DetalleIngreso(models.Model):
    id = models.AutoField(primary_key=True)
    id_ingreso = models.ForeignKey(Ingreso, blank=True, null=True)
    codigo_producto = models.ForeignKey(Producto, blank=True, null=True)
    serie = models.CharField(max_length=20, blank=True, null=True)
    cantidad = models.IntegerField(blank=True, null=True)
    unidad_caja = models.IntegerField(blank=True, null=True)
    estado = models.CharField(max_length=15, blank=True, null=True)


class Almacen(models.Model):
    id = models.AutoField(primary_key=True)
    ubicacion = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        verbose_name_plural = "Almacenes"


class DetalleAlmacen(models.Model):
    id = models.AutoField(primary_key=True)
    codigo_producto = models.ForeignKey(Producto)
    id_almacen = models.ForeignKey(Almacen)
    id_ingreso = models.ForeignKey(Ingreso, blank=True, null=True)
    cantidad = models.IntegerField()
    estado = models.CharField(max_length=10, blank=True, null=True)


class Salida(models.Model):
    id = models.AutoField(primary_key=True)
    dni_usuario = models.ForeignKey(User)
    id_almacen = models.ForeignKey(Almacen)
    fecha = models.DateField(blank=True, null=True)
    nodo = models.CharField(max_length=15, blank=True, null=True)
    devolucion = models.NullBooleanField()


class DetalleSalida(models.Model):
    id = models.AutoField(primary_key=True)
    codigo_producto = models.ForeignKey(Producto, blank=True, null=True)
    id_salida = models.ForeignKey(Salida, blank=True, null=True)
    cantidad = models.IntegerField(blank=True, null=True)


# guia de remision - campo proveedores