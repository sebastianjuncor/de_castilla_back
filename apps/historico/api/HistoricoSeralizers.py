from rest_framework import serializers

from ..models import *
from rest_framework import serializers
from apps.insumo.api.InsumoSeralizers import InsumoSeralizers
from apps.producto.api.ProductoSeralizers import ProductoSerializer
from apps.tipo_movimiento.api.TipoMovientoSeralizers import TipoMovientoSeralizer




class HistoricoSeralizers(serializers.ModelSerializer):
    insumo = InsumoSeralizers(source='id_insumo_fk', read_only=True)
    producto = ProductoSerializer(source='id_producto_fk', read_only=True)
    tipo_movimiento = TipoMovientoSeralizer(source='id_tipo_movimiento_fk', read_only=True)
    class Meta:
        model = Historico
        fields = '__all__'  # Incluir todos los campos del modelo