from apps.usuarios.models import User
from rest_framework import serializers
from .models import Salida


class SalidaSerializer(serializers.ModelSerializer):
    dni_usuario = serializers.SlugRelatedField(queryset=User.objects.filter(), slug_field='dni_usuario')

    class Meta:
        model = Salida
        fields = ('dni_usuario', 'id_almacen', 'fecha', 'nodo', 'devolucion')
