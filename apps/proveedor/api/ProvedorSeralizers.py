from rest_framework import serializers
from ..models import *
from rest_framework import serializers




class ProveedorSeralizers(serializers.ModelSerializer):
    class Meta:
        model = Proveedor
        fields = '__all__'  # Incluir todos los campos del modelo