# Description: Modelo de la tabla detalle_pedido.
# The code is similar to apps/detalle_oc/models.py
from django.db import models
from apps.pedido.models import Pedido
from apps.producto.models import Producto

class DetallePedido(models.Model):
    id_detalle_pedido = models.AutoField(primary_key=True)
    cantidad_producto = models.IntegerField()
    subtotal_detalle_pedido = models.IntegerField()
    id_producto_fk = models.ForeignKey(Producto, db_column='id_producto_fk', on_delete=models.CASCADE, blank=True, null=True)
    id_pedido_fk = models.ForeignKey(Pedido, db_column='id_pedido_fk', on_delete=models.CASCADE, blank=True, null=True)
    estado = models.BooleanField(default=True)

    class Meta:
        db_table = 'detalle_pedido'