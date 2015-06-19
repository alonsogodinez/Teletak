from django.contrib import admin
from .models import *
# Register your models here.

class CategoriaAdmin(admin.ModelAdmin):
    model=Categoria
class ProductosAdmin(admin.ModelAdmin):
    model = Producto
    list_display = ('codigo','sap','descripcion','categoria','stock_minimo',)
    list_editable = ('codigo','sap','descripcion','categoria','stock_minimo',)

admin.site.register(Producto,ProductosAdmin)
admin.site.register(Categoria,CategoriaAdmin)