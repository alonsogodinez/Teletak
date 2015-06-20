from django.contrib import admin
from .models import *
from apps.almacen.models import *
# Register your models here.

class CategoriaAdmin(admin.ModelAdmin):
    model=Categoria
class ProductosAdmin(admin.ModelAdmin):
    model = Producto
    list_display = ('codigo','sap','descripcion','categoria','stock_minimo',)
    list_editable = ('codigo','sap','descripcion','categoria','stock_minimo',)

class GuiaDeRemisionAdmin(admin.ModelAdmin):
    model = GuiaRemision
    list_display = ('id','fecha_traslado','punto_partida','nro_guia_remitente','placa_vehiculo','licencia_conducir')
    list_editable = ('id','fecha_traslado','punto_partida','nro_guia_remitente','placa_vehiculo','licencia_conducir')

admin.site.register(Producto,ProductosAdmin)
admin.site.register(Categoria,CategoriaAdmin)
admin.site.register(GuiaRemision,GuiaDeRemisionAdmin)
