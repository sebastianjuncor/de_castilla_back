from rest_framework import serializers

from .models import *

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'

class EstadoInsumoSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstadoInsumo
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
