from rest_framework import serializers

from ..models import *
from rest_framework import serializers
from apps.estado_pedido.api.EstadoPedidoSeralizers import EstadoPedidoSeralizers
from apps.usuarios.api.UsuarioSeralizers import UsuarioSerializer




class PedidoSeralizers(serializers.ModelSerializer):
    estado_pedido = EstadoPedidoSeralizers(source='id_estado_pedido_fk', read_only=True)  # Relación con el modelo EstadoPedido
    usuario = UsuarioSerializer(source='no_Documento_Usuario_fk', read_only=True)  # Relación con el modelo Usuario
    class Meta:
        model = Pedido
        fields = '__all__'  # Incluir todos los campos del modelo