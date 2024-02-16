from rest_framework import serializers
from ..models import *
from rest_framework import serializers




class EstadoPedidoSeralizers(serializers.ModelSerializer):
    class Meta:
        model = EstadoPedido
        fields = '__all__'  # Incluir todos los campos del modelo