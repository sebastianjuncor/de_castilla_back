from rest_framework import serializers
from ..models import *
from rest_framework import serializers




class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'  # Incluir todos los campos del modelo