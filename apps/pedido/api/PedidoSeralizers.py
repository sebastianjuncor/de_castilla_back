from rest_framework import serializers
from ..models import *
from rest_framework import serializers




class PedidoSeralizers(serializers.ModelSerializer):
    class Meta:
        model = Pedido
        fields = '__all__'  # Incluir todos los campos del modelo