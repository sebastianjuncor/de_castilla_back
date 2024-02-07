from rest_framework import serializers
from .models import *

class EstadoPedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstadoPedido
        fields = '__all__'

class ProveedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proveedor
        fields = '__all__'

class RolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rol
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

class PermisoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permiso
        fields = '__all__'

class SaborSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sabor
        fields = '__all__'

class TipoMovimientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoMovimiento
        fields = '__all__'

class UsuarioSerializer(serializers.ModelSerializer):
    rol = RolSerializer(source = 'id_rol_fk', read_only = True)
    class Meta:
        model = Usuario
        fields = '__all__'

class PedidoSerializer(serializers.ModelSerializer):
    pedido = EstadoPedidoSerializer(source = 'id_estado_pedido_fk', read_only = True)
    usuario = UsuarioSerializer(source = 'no_documento_usuario_fk', read_only = True)
    class Meta:
        model = Pedido
        fields = '__all__'

class VentaSerializer(serializers.ModelSerializer):
    pedido = PedidoSerializer(source = 'id_pedido_fk', read_only = True)
    class Meta:
        model = Venta
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

class RolHasPermisoSerializer(serializers.ModelSerializer):
    permiso = PermisoSerializer(source = 'id_permiso_fk', read_only = True)
    rol = RolSerializer(source = 'id_rol_fk', read_only = True)
    class Meta:
        model = RolHasPermiso
        fields = '__all__'

class OrdenCompraSerializer(serializers.ModelSerializer):
    estado_oc = EstadoOcSerializer(source = 'id_estado_oc_fk', read_only = True)
    class Meta:
        model = OrdenCompra
        fields = '__all__'

class CalificacionSerializer(serializers.ModelSerializer):
    pedido = PedidoSerializer(source = 'id_pedido_fk', read_only = True)
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

class DetallePedidoSerializer(serializers.ModelSerializer):
    producto = ProductoSerializer(source = 'id_producto_fk', read_only = True)
    pedido = PedidoSerializer(source = 'id_pedido_fk', read_only = True)
    class Meta:
        model = DetallePedido
        fields = '__all__'

class DetalleVentaSerializer(serializers.ModelSerializer):
    producto = ProductoSerializer(source = 'id_producto_fk', read_only = True)
    venta = VentaSerializer(source = 'id_venta_fk', read_only = True)
    class Meta:
        model = DetalleVenta
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

