from django.contrib import admin
from .models import *
from apps.almacen.models import *
# Register your models here.

class CategoriaAdmin(admin.ModelAdmin):
    model=Categoria
class ProductosAdmin(admin.ModelAdmin):
    model = Producto
    list_display = ('sap','descripcion','categoria','stock_minimo',)
    list_editable = ('descripcion','categoria','stock_minimo',)

class ProductoMedidaAdmin(admin.ModelAdmin):
    model = ProductoMedida
    list_display = ('codigo_producto','id_unidad','equivalencia',)
    list_editable = ('id_unidad','equivalencia',)

class UnidadMedicionAdmin(admin.ModelAdmin):
    model = UnidadMedicion
    def __unicode__(self):
        return 'Unidades de Medida'


class GuiaDeRemisionAdmin(admin.ModelAdmin):
    model = GuiaRemision
    list_display = ('id','fecha_traslado','punto_partida','nro_guia_remitente','placa_vehiculo','licencia_conducir')
    list_editable = ('id','fecha_traslado','punto_partida','nro_guia_remitente','placa_vehiculo','licencia_conducir')

admin.site.register(Producto,ProductosAdmin)
admin.site.register(Categoria,CategoriaAdmin)
admin.site.register(ProductoMedida,ProductoMedidaAdmin)
admin.site.register(UnidadMedicion,UnidadMedicionAdmin)
admin.site.register(GuiaRemision,GuiaDeRemisionAdmin)
