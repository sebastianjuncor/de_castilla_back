from rest_framework import serializers

from ..models import *
from rest_framework import serializers
from apps.pedido.api.PedidoSeralizers import PedidoSeralizers
from apps.producto.api.ProductoSeralizers import ProductoSerializer




class DetallePedidoSeralizers(serializers.ModelSerializer):
    producto = ProductoSerializer(source='id_producto_fk', read_only=True)
    pedido = PedidoSeralizers(source='id_pedido_fk', read_only=True)
    class Meta:
        model = DetallePedido
        fields = '__all__'  # Incluir todos los campos del modelo