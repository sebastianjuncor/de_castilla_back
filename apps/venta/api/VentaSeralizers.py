from rest_framework import serializers
from ..models import *
from rest_framework import serializers




class VentaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venta
        fields = '__all__'  # Incluir todos los campos del modelo