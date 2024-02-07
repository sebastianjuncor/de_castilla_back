# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Calificacion(models.Model):
    id_calificacion = models.BigAutoField(primary_key=True)
    comentario_calificacion = models.CharField(max_length=255, blank=True, null=True)
    estrallas_calificacion = models.IntegerField(blank=True, null=True)
    id_proveedor_fk = models.ForeignKey('Proveedor', models.DO_NOTHING, db_column='id_proveedor_fk', blank=True, null=True)
    estado = models.BooleanField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'calificacion'


class Categoria(models.Model):
    id_categoria = models.BigAutoField(primary_key=True)
    descripcion_categoria = models.CharField(max_length=255, blank=True, null=True)
    nombre_categoria = models.CharField(max_length=255, blank=True, null=True)
    estado = models.BooleanField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'categoria'


class DetalleOc(models.Model):
    id_detalle_oc = models.BigAutoField(primary_key=True)
    cantidad_insumo = models.IntegerField(blank=True, null=True)
    id_insumo_fk = models.ForeignKey('Insumo', models.DO_NOTHING, db_column='id_insumo_fk', blank=True, null=True)
    id_oc_fk = models.ForeignKey('OrdenCompra', models.DO_NOTHING, db_column='id_oc_fk', blank=True, null=True)
    estado = models.BooleanField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'detalle_oc'


class DetallePedido(models.Model):
    id_detalle_pedido = models.BigAutoField(primary_key=True)
    cantidad_producto = models.IntegerField(blank=True, null=True)
    subtotal_detalle_pedido = models.BigIntegerField(blank=True, null=True)
    id_producto_fk = models.ForeignKey('Producto', models.DO_NOTHING, db_column='id_producto_fk', blank=True, null=True)
    id_pedido_fk = models.ForeignKey('Pedido', models.DO_NOTHING, db_column='id_pedido_fk', blank=True, null=True)
    estado = models.BooleanField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'detalle_pedido'


class DetalleVenta(models.Model):
    id_detalle_venta = models.BigAutoField(primary_key=True)
    cantidad_producto = models.IntegerField(blank=True, null=True)
    subtotal_detalle_venta = models.BigIntegerField(blank=True, null=True)
    id_producto_fk = models.ForeignKey('Producto', models.DO_NOTHING, db_column='id_producto_fk', blank=True, null=True)
    id_venta_fk = models.ForeignKey('Venta', models.DO_NOTHING, db_column='id_venta_fk', blank=True, null=True)
    estado = models.BooleanField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'detalle_venta'


class EstadoInsumo(models.Model):
    id_estado_insumo = models.BigAutoField(primary_key=True)
    nombre_estado_insumo = models.CharField(max_length=255, blank=True, null=True)
    estado = models.BooleanField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'estado_insumo'


class EstadoOc(models.Model):
    id_estado_oc = models.BigAutoField(primary_key=True)
    nombre_estado_oc = models.CharField(max_length=255, blank=True, null=True)
    estado = models.BooleanField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'estado_oc'


class EstadoPedido(models.Model):
    id_estado_pedido = models.BigAutoField(primary_key=True)
    nombre_estado = models.CharField(max_length=255, blank=True, null=True)
    estado = models.BooleanField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'estado_pedido'


class Historico(models.Model):
    id_historico = models.BigAutoField(primary_key=True)
    cantidad_historico = models.IntegerField(blank=True, null=True)
    fecha_caducidad = models.DateField(blank=True, null=True)
    fecha_movimiento = models.DateField(blank=True, null=True)
    tipo_historico = models.CharField(max_length=255, blank=True, null=True)
    id_insumo_fk = models.ForeignKey('Insumo', models.DO_NOTHING, db_column='id_insumo_fk', blank=True, null=True)
    id_producto_fk = models.ForeignKey('Producto', models.DO_NOTHING, db_column='id_producto_fk', blank=True, null=True)
    id_tipo_movimiento_fk = models.ForeignKey('TipoMovimiento', models.DO_NOTHING, db_column='id_tipo_movimiento_fk', blank=True, null=True)
    estado = models.BooleanField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'historico'


class Insumo(models.Model):
    id_insumo = models.BigAutoField(primary_key=True)
    nombre_insumo = models.CharField(max_length=255, blank=True, null=True)
    id_estado_insumo = models.ForeignKey(EstadoInsumo, models.DO_NOTHING, db_column='id_estado_insumo', blank=True, null=True)
    estado = models.BooleanField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'insumo'


class Inventario(models.Model):
    id_inventario = models.BigAutoField(primary_key=True)
    stock_inventario = models.IntegerField(blank=True, null=True)
    tipo_inventario = models.CharField(max_length=255, blank=True, null=True)
    id_insumo_fk = models.ForeignKey(Insumo, models.DO_NOTHING, db_column='id_insumo_fk', blank=True, null=True)
    id_producto_fk = models.ForeignKey('Producto', models.DO_NOTHING, db_column='id_producto_fk', blank=True, null=True)
    estado = models.BooleanField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'inventario'


class OcHasProveedor(models.Model):
    id_oc_has_proveedor = models.BigAutoField(primary_key=True)
    id_oc_fk = models.ForeignKey('OrdenCompra', models.DO_NOTHING, db_column='id_oc_fk', blank=True, null=True)
    id_proveedor_fk = models.ForeignKey('Proveedor', models.DO_NOTHING, db_column='id_proveedor_fk', blank=True, null=True)
    estado = models.BooleanField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'oc_has_proveedor'


class OrdenCompra(models.Model):
    id_oc = models.BigAutoField(primary_key=True)
    fecha_oc = models.DateField(blank=True, null=True)
    hora_oc = models.TimeField(blank=True, null=True)
    id_estado_oc_fk = models.ForeignKey(EstadoOc, models.DO_NOTHING, db_column='id_estado_oc_fk', blank=True, null=True)
    estado = models.BooleanField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'orden_compra'


class Pedido(models.Model):
    id_pedido = models.BigAutoField(primary_key=True)
    descripcion_pedido = models.CharField(max_length=255, blank=True, null=True)
    fecha_pedido = models.DateField(blank=True, null=True)
    id_estado_pedido_fk = models.ForeignKey(EstadoPedido, models.DO_NOTHING, db_column='id_estado_pedido_fk', blank=True, null=True)
    no_documento_usuario_fk = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='no_documento_usuario_fk', blank=True, null=True)
    estrellas_pedido = models.IntegerField(blank=True, null=True)
    comentario_pedido = models.CharField(max_length=100, blank=True, null=True)
    estado = models.BooleanField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'pedido'


class Permiso(models.Model):
    id_permiso = models.BigAutoField(primary_key=True)
    descripcion_permiso = models.CharField(max_length=255, blank=True, null=True)
    estado = models.BooleanField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'permiso'


class Producto(models.Model):
    id_producto = models.BigAutoField(primary_key=True)
    nombre_producto = models.CharField(max_length=255, blank=True, null=True)
    imagen_producto = models.CharField(max_length=255, blank=True, null=True)
    precio_producto = models.IntegerField(blank=True, null=True)
    id_categoria_fk = models.ForeignKey(Categoria, models.DO_NOTHING, db_column='id_categoria_fk', blank=True, null=True)
    estado = models.BooleanField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'producto'


class Proveedor(models.Model):
    id_proveedor = models.BigAutoField(primary_key=True)
    celular_proveedor = models.BigIntegerField(blank=True, null=True)
    celular_respaldo_proveedor = models.BigIntegerField(blank=True, null=True)
    correo_proveedor = models.CharField(max_length=255, blank=True, null=True)
    empresa_proveedor = models.CharField(max_length=255, blank=True, null=True)
    estado_proveedor = models.BooleanField() # This field type is a guess.
    nit_proveedor = models.BigIntegerField(blank=True, null=True)
    nombre_proveedor = models.CharField(max_length=255, blank=True, null=True)
    estado = models.BooleanField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'proveedor'


class Rol(models.Model):
    id_rol = models.BigAutoField(primary_key=True)
    nombre_rol = models.CharField(max_length=255, blank=True, null=True)
    estado = models.BooleanField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'rol'


class RolHasPermiso(models.Model):
    id_rol_has_permiso = models.BigAutoField(primary_key=True)
    id_permiso_fk = models.ForeignKey(Permiso, models.DO_NOTHING, db_column='id_permiso_fk', blank=True, null=True)
    id_rol_fk = models.ForeignKey(Rol, models.DO_NOTHING, db_column='id_rol_fk', blank=True, null=True)
    estado = models.BooleanField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'rol_has_permiso'


class Sabor(models.Model):
    id_sabor = models.BigAutoField(primary_key=True)
    nombre_sabor = models.CharField(max_length=255, blank=True, null=True)
    estado = models.BooleanField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'sabor'


class SaborHasProducto(models.Model):
    id_sabor_has_producto = models.BigAutoField(primary_key=True)
    id_producto_fk = models.ForeignKey(Producto, models.DO_NOTHING, db_column='id_producto_fk', blank=True, null=True)
    id_sabor_fk = models.ForeignKey(Sabor, models.DO_NOTHING, db_column='id_sabor_fk', blank=True, null=True)
    estado = models.BooleanField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'sabor_has_producto'


class TipoMovimiento(models.Model):
    id_tipo_movimiento = models.BigAutoField(primary_key=True)
    nombre_tipo_movimiento = models.CharField(max_length=255, blank=True, null=True)
    estado = models.BooleanField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'tipo_movimiento'


class Usuario(models.Model):
    no_documento_usuario = models.BigAutoField(primary_key=True)
    apellido_usuario = models.CharField(max_length=255, blank=True, null=True)
    celular_usuario = models.BigIntegerField(blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    nombre_usuario = models.CharField(max_length=255, blank=True, null=True)
    password = models.CharField(max_length=255, blank=True, null=True)
    id_rol_fk = models.ForeignKey(Rol, models.DO_NOTHING, db_column='id_rol_fk', blank=True, null=True)
    estado = models.BooleanField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'usuario'


class Venta(models.Model):
    id_venta = models.BigAutoField(primary_key=True)
    fecha_venta = models.DateField(blank=True, null=True)
    hora_venta = models.TimeField(blank=True, null=True)
    total_venta = models.BigIntegerField(blank=True, null=True)
    id_pedido_fk = models.ForeignKey(Pedido, models.DO_NOTHING, db_column='id_pedido_fk', blank=True, null=True)
    no_documento_usuario_fk = models.ForeignKey(Usuario, models.DO_NOTHING, db_column='no_documento_usuario_fk', blank=True, null=True)
    estado = models.BooleanField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'venta'
