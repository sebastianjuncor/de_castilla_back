from rest_framework import serializers
from ..models import *

from rest_framework import serializers
from apps.producto.api.ProductoSeralizers import ProductoSerializer
from apps.sabor.api.SaborSeralizers import SaborSerializer




class SaborHasProductoSeralizer(serializers.ModelSerializer):
    producto = ProductoSerializer(source='id_producto_fk', read_only=True)
    sabor = SaborSerializer(source='id_sabor_fk', read_only=True)
    class Meta:
        model = SaborHasProducto
        fields = '__all__'  # Incluir todos los campos del modelo