from rest_framework import serializers

from ..models import *
from rest_framework import serializers
from apps.producto.api.ProductoSeralizers import ProductoSerializer
from apps.venta.api.VentaSeralizers import VentaSerializer




class DetalleVentaSeralizers(serializers.ModelSerializer):
    producto = ProductoSerializer(source='id_producto_fk', read_only=True)
    venta = VentaSerializer(source='id_venta_fk', read_only=True)
    class Meta:
        model = DetalleVenta
        fields = '__all__'  # Incluir todos los campos del modelo