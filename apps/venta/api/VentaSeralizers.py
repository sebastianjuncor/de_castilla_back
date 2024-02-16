from rest_framework import serializers

from apps.pedido.api.PedidoSeralizers import PedidoSeralizers
from apps.usuarios.api.UsuarioSeralizers import UsuarioSerializer
from ..models import *
from rest_framework import serializers




class VentaSerializer(serializers.ModelSerializer):
    pedido = PedidoSeralizers(source='id_pedido_fk', read_only=True)
    usuario = UsuarioSerializer(source='no_documento_usuario_fk', read_only=True)
    class Meta:
        model = Venta
        fields = '__all__'  # Incluir todos los campos del modelo