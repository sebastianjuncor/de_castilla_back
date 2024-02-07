from rest_framework import serializers

from .models import *

class ProveedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proveedor
        fields = '__all__'

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'


class EstadoInsumoSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstadoInsumo
        fields = '__all__'

class EstadoOcSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstadoOc
        fields = '__all__'

class InsumoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Insumo
        fields = '__all__'

class SaborSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sabor
        fields = '__all__'

class TipoMovimientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoMovimiento
        fields = '__all__'


class ProductoSerializer(serializers.ModelSerializer):
    categoria = CategoriaSerializer(source = 'id_categoria_fk', read_only = True)
    class Meta:
        model = Producto
        fields = '__all__'

class SaborHasProductoSerializer(serializers.ModelSerializer):
    producto = ProductoSerializer(source = 'id_producto_fk', read_only = True)
    sabor = SaborSerializer(source = 'id_sabor_fk', read_only = True)
    class Meta:
        model = SaborHasProducto
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

class HistoricoSerializer(serializers.ModelSerializer):
    insumo = InsumoSerializer(source = 'id_insumo_fk', read_only = True)
    producto = ProductoSerializer(source = 'id_producto_fk', read_only = True)
    tipo_movimiento = TipoMovimientoSerializer(source = 'id_tipo_movimiento_fk', read_only = True)
    class Meta:
        model = Historico
        fields = '__all__'

class InventarioSerializer(serializers.ModelSerializer):
    insumo = InsumoSerializer(source = 'id_insumo_fk', read_only = True)
    producto = ProductoSerializer(source = 'id_producto_fk', read_only = True)
    class Meta:
        model = Inventario
        fields = '__all__'

class OcHasProveedorSerializer(serializers.ModelSerializer):
    orden_compra = OrdenCompraSerializer(source = 'id_oc_fk', read_only = True)
    proveedor = ProveedorSerializer(source = 'id_proveedor_fk', read_only = True)
    class Meta:
        model = OcHasProveedor
        fields = '__all__'

