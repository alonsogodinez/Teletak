from django.contrib import admin
from .models import *

@admin.register(Almacen)
class AlmacenAdmin(admin.ModelAdmin):
    pass

class ProveedorAdmin(admin.ModelAdmin):
    model = Proveedor
    list_display = ('ruc','nombre','direccion')
    list_edit = ('ruc','nombre','direccion')

admin.site.register(Proveedor,ProveedorAdmin)

@admin.register(Ingreso)
class IngresoAdmin(admin.ModelAdmin):
    model = Ingreso


@admin.register(DetalleIngreso)
class DetalleIngresoAdmin  (admin.ModelAdmin):
    model = DetalleIngreso