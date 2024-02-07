from django.db import models
from inventarios.models import Producto

from usuarios.models import Usuario

class EstadoPedido(models.Model):
    id_estado_pedido = models.BigAutoField(primary_key=True)
    nombre_estado = models.CharField(max_length=255, blank=True, null=True)
    estado = models.BooleanField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'estado_pedido'

class Pedido(models.Model):
    id_pedido = models.BigAutoField(primary_key=True)
    descripcion_pedido = models.CharField(max_length=255, blank=True, null=True)
    fecha_pedido = models.DateField(blank=True, null=True)
    id_estado_pedido_fk = models.ForeignKey(EstadoPedido, models.DO_NOTHING, db_column='id_estado_pedido_fk', blank=True, null=True)
    no_documento_usuario_fk = models.ForeignKey(Usuario, models.DO_NOTHING, db_column='no_documento_usuario_fk', blank=True, null=True)
    estrellas_pedido = models.IntegerField(blank=True, null=True)
    comentario_pedido = models.CharField(max_length=100, blank=True, null=True)
    estado = models.BooleanField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'pedido'

class DetallePedido(models.Model):
    id_detalle_pedido = models.BigAutoField(primary_key=True)
    cantidad_producto = models.IntegerField(blank=True, null=True)
    subtotal_detalle_pedido = models.BigIntegerField(blank=True, null=True)
    id_producto_fk = models.ForeignKey(Producto, models.DO_NOTHING, db_column='id_producto_fk', blank=True, null=True)
    id_pedido_fk = models.ForeignKey(Pedido, models.DO_NOTHING, db_column='id_pedido_fk', blank=True, null=True)
    estado = models.BooleanField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'detalle_pedido'
