from rest_framework import serializers

from usuarios.serializers import UsuarioSerializer


from .models import *
from api.serializers import ProductoSerializer
from pedidos.serializers import PedidoSerializer

class VentaSerializer(serializers.ModelSerializer):
    pedido = PedidoSerializer(source = 'id_pedido_fk', read_only = True)
    usuario = UsuarioSerializer(source = 'no_documento_usuario_fk', read_only = True)

    class Meta:
        model = Venta
        fields = '__all__'

class DetalleVentaSerializer(serializers.ModelSerializer):
    producto = ProductoSerializer(source = 'id_producto_fk', read_only = True)
    venta = VentaSerializer(source = 'id_venta_fk', read_only = True)
    class Meta:
        model = DetalleVenta
        fields = '__all__'
