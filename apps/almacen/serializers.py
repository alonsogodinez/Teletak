from apps.usuarios.models import User
from rest_framework import serializers
from .models import Salida


class SalidaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Salida
        fields = ('id','dni_usuario', 'id_almacen', 'fecha', 'nodo', 'devolucion')

