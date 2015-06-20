from django.contrib import admin
from .models import *
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


admin.site.register(Producto,ProductosAdmin)
admin.site.register(Categoria,CategoriaAdmin)
admin.site.register(ProductoMedida,ProductoMedidaAdmin)
admin.site.register(UnidadMedicion,UnidadMedicionAdmin)
