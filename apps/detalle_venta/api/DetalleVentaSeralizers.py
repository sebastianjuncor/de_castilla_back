from rest_framework import serializers
from ..models import *
from rest_framework import serializers




class DetalleVentaSeralizers(serializers.ModelSerializer):
    class Meta:
        model = DetalleVenta
        fields = '__all__'  # Incluir todos los campos del modelo