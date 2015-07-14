from django.contrib import admin
from .models import *


@admin.register(Almacen)
class AlmacenAdmin(admin.ModelAdmin):
    model = Almacen
    list_display = ('id',)

class ProveedorAdmin(admin.ModelAdmin):
    model = Proveedor
    list_display = ('ruc','nombre','direccion')
    list_edit = ('ruc','nombre','direccion')

class SalidaAdmin(admin.ModelAdmin):
    model=Salida
    list_display = ('id','dni_usuario','fecha','nodo','devolucion',)

class DetalleSalidaAdmin(admin.ModelAdmin):
    model = DetalleSalida
    list_display = ('id_salida','codigo_producto','cantidad','id_almacen')
    list_editable = ('codigo_producto','cantidad')

class DetalleAlmacenAdmin(admin.ModelAdmin):
    model = DetalleAlmacen
    list_display = ('id','codigo_producto','cantidad','id_almacen')

@admin.register(DetalleStock)
class StockAdmin(admin.ModelAdmin):
    model = DetalleStock
    list_display = ('id_almacen','producto','stock')

admin.site.register(Proveedor,ProveedorAdmin)
admin.site.register(Salida,SalidaAdmin)
admin.site.register(DetalleSalida,DetalleSalidaAdmin)
admin.site.register(DetalleAlmacen,DetalleAlmacenAdmin)



@admin.register(Ingreso)
class IngresoAdmin(admin.ModelAdmin):
    model = Ingreso


@admin.register(DetalleIngreso)
class DetalleIngresoAdmin  (admin.ModelAdmin):
    model = DetalleIngreso
