from rest_framework import serializers
from ..models import *
from rest_framework import serializers




class InventarioSeralizers(serializers.ModelSerializer):
    class Meta:
        model = Inventario
        fields = '__all__'  # Incluir todos los campos del modelo