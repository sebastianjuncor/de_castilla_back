from rest_framework import serializers

from api.serializers import ProductoSerializer
from usuarios.serializers import UsuarioSerializer
from .models import *

class EstadoPedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstadoPedido
        fields = '__all__'

class PedidoSerializer(serializers.ModelSerializer):
    estado_pedido = EstadoPedidoSerializer(source = 'id_estado_pedido_fk', read_only = True)
    usuario = UsuarioSerializer(source = 'no_documento_usuario_fk', read_only = True)
    class Meta:
        model = Pedido
        fields = '__all__'


class DetallePedidoSerializer(serializers.ModelSerializer):
    producto = ProductoSerializer(source = 'id_producto_fk', read_only = True)
    pedido = PedidoSerializer(source = 'id_pedido_fk', read_only = True)
    class Meta:
        model = DetallePedido
        fields = '__all__'
