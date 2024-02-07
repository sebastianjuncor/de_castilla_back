from django.db import models

class Categoria(models.Model):
    id_categoria = models.BigAutoField(primary_key=True)
    descripcion_categoria = models.CharField(max_length=255, blank=True, null=True)
    nombre_categoria = models.CharField(max_length=255, blank=True, null=True)
    estado = models.BooleanField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'categoria'

class EstadoInsumo(models.Model):
    id_estado_insumo = models.BigAutoField(primary_key=True)
    nombre_estado_insumo = models.CharField(max_length=255, blank=True, null=True)
    estado = models.BooleanField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'estado_insumo'

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

