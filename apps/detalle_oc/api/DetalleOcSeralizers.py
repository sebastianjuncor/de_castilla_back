from rest_framework import serializers

from ..models import *
from rest_framework import serializers
from apps.insumo.api.InsumoSeralizers import InsumoSeralizers
from apps.orden_compra.api.OrdenCompraSeralizers import OrdenCompraSeralizers




class DetalleOCSeralizers(serializers.ModelSerializer):
    insumo = InsumoSeralizers(source='id_insumo_fk', read_only=True)
    orden_compra = OrdenCompraSeralizers(source='id_oc_fk', read_only=True)
    class Meta:
        model = DetalleOC
        fields = '__all__'  # Incluir todos los campos del modelo