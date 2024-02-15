from rest_framework import serializers
from ..models import *
from rest_framework import serializers




class DetallePedidoSeralizers(serializers.ModelSerializer):
    class Meta:
        model = DetallePedido
        fields = '__all__'  # Incluir todos los campos del modelo