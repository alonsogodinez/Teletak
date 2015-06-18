from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,UserManager


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=50, unique=True)
    dni = models.CharField(primary_key=True, max_length=8)

    nombre = models.CharField(max_length=30, blank=True, null=True)
    apellido = models.CharField(max_length=30, blank=True, null=True)
    telefono = models.CharField(max_length=15, blank=True, null=True)
    celular = models.CharField(max_length=15, blank=True, null=True)
    tipo_usuario = models.CharField(max_length=10, blank=True, null=True)

    objects = UserManager()

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'

    def get_short_name(self):
        return self.username

    def get_full_name(self):
        return self.nombre+' '+self.apellido

class Almacen(models.Model):
    id = models.SmallIntegerField(primary_key=True)
    ubicacion = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'almacen'


class DetalleAlmacen(models.Model):
    id = models.SmallIntegerField(primary_key=True)
    codigo_producto = models.ForeignKey('Producto', db_column='codigo_producto')
    id_almacen = models.ForeignKey(Almacen, db_column='id_almacen')
    id_ingreso = models.ForeignKey('Ingreso', db_column='id_ingreso', blank=True, null=True)
    cantidad = models.IntegerField()
    estado = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'detalle_almacen'


class DetalleIngreso(models.Model):
    id = models.SmallIntegerField(primary_key=True)
    id_ingreso = models.ForeignKey('Ingreso', db_column='id_ingreso', blank=True, null=True)
    codigo_producto = models.ForeignKey('Producto', db_column='codigo_producto', blank=True, null=True)
    serie = models.CharField(max_length=20, blank=True, null=True)
    cantidad = models.IntegerField(blank=True, null=True)
    unidad_caja = models.IntegerField(blank=True, null=True)
    estado = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'detalle_ingreso'


class DetalleSalida(models.Model):
    id = models.SmallIntegerField(primary_key=True)
    codigo_producto = models.ForeignKey('Producto', db_column='codigo_producto', blank=True, null=True)
    id_salida = models.ForeignKey('Salida', db_column='id_salida', blank=True, null=True)
    cantidad = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'detalle_salida'


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class Ingreso(models.Model):
    id = models.IntegerField(primary_key=True)
    dni_usuario = models.ForeignKey('Usuario', db_column='dni_usuario', blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)
    guia_remision = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ingreso'


class Producto(models.Model):
    codigo = models.CharField(primary_key=True, max_length=10)
    sap = models.CharField(max_length=10, blank=True, null=True)
    descripcion = models.CharField(max_length=50, blank=True, null=True)
    und_med_basica = models.CharField(max_length=5, blank=True, null=True)
    und_med_secundaria = models.CharField(max_length=5, blank=True, null=True)
    categoria = models.CharField(max_length=10, blank=True, null=True)
    stock_minimo = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'producto'


class Salida(models.Model):
    id = models.IntegerField(primary_key=True)
    dni_usuario = models.ForeignKey('Usuario', db_column='dni_usuario')
    id_almacen = models.ForeignKey(Almacen, db_column='id_almacen')
    fecha = models.DateField(blank=True, null=True)
    nodo = models.CharField(max_length=15, blank=True, null=True)
    devolucion = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'salida'


class Usuario(models.Model):
    dni = models.CharField(primary_key=True, max_length=8)
    nombre = models.CharField(max_length=30, blank=True, null=True)
    apellido = models.CharField(max_length=30, blank=True, null=True)
    telefono = models.CharField(max_length=15, blank=True, null=True)
    celular = models.CharField(max_length=15, blank=True, null=True)
    tipo_usuario = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'usuario'