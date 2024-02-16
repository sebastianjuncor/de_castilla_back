from rest_framework import serializers

from ..models import *
from rest_framework import serializers
from apps.orden_compra.api.OrdenCompraSeralizers import OrdenCompraSeralizers
from apps.proveedor.api.ProvedorSeralizers import ProveedorSeralizers




class OcHasProvedorSeralizers(serializers.ModelSerializer):
    orden_compra = OrdenCompraSeralizers(source='id_oc_fk', read_only=True)
    proveedor = ProveedorSeralizers(source='id_proveedor_fk', read_only=True)
    class Meta:
        model = OCHasProveedor
        fields = '__all__'  # Incluir todos los campos del modelo