from django.contrib import admin
from .models import Almacen

@admin.register(Almacen)
class AlmacenAdmin(admin.ModelAdmin):
    pass