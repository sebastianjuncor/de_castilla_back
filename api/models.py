from django.db import models

from pedidos.models import Pedido
from usuarios.models import Usuario


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

