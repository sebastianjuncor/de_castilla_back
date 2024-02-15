from rest_framework import serializers
from ..models import *
from rest_framework import serializers




class OrdenCompraSeralizers(serializers.ModelSerializer):
    class Meta:
        model = OrdenCompra
        fields = '__all__'  # Incluir todos los campos del modelo