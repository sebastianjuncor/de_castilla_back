from django.db import models
from inventarios.models import Producto

from pedidos.models import Pedido
from usuarios.models import Usuario
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

class DetalleVenta(models.Model):
    id_detalle_venta = models.BigAutoField(primary_key=True)
    cantidad_producto = models.IntegerField(blank=True, null=True)
    subtotal_detalle_venta = models.BigIntegerField(blank=True, null=True)
    id_producto_fk = models.ForeignKey(Producto, models.DO_NOTHING, db_column='id_producto_fk', blank=True, null=True)
    id_venta_fk = models.ForeignKey(Venta, models.DO_NOTHING, db_column='id_venta_fk', blank=True, null=True)
    estado = models.BooleanField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'detalle_venta'
