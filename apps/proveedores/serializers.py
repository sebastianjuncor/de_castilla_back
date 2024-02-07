from rest_framework import serializers

from inventarios.serializers import InsumoSerializer

from .models import *

class ProveedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proveedor
        fields = '__all__'

class EstadoOcSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstadoOc
        fields = '__all__'

class OrdenCompraSerializer(serializers.ModelSerializer):
    estado_oc = EstadoOcSerializer(source = 'id_estado_oc_fk', read_only = True)
    class Meta:
        model = OrdenCompra
        fields = '__all__'

class CalificacionSerializer(serializers.ModelSerializer):
    proveedor = ProveedorSerializer(source = 'id_proveedor_fk', read_only = True)
    class Meta:
        model = Calificacion
        fields = '__all__'

class DetalleOcSerializer(serializers.ModelSerializer):
    insumo = InsumoSerializer(source = 'id_insumo_fk', read_only = True)
    orden_compra = OrdenCompraSerializer(source = 'id_oc_fk', read_only = True)
    class Meta:
        model = DetalleOc
        fields = '__all__'

class OcHasProveedorSerializer(serializers.ModelSerializer):
    orden_compra = OrdenCompraSerializer(source = 'id_oc_fk', read_only = True)
    proveedor = ProveedorSerializer(source = 'id_proveedor_fk', read_only = True)
    class Meta:
        model = OcHasProveedor
        fields = '__all__'

