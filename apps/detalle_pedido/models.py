# Description: Modelo de la tabla detalle_pedido.
# The code is similar to apps/detalle_oc/models.py
from django.db import models
from apps.pedido.models import Pedido
from apps.producto.models import Producto

class DetallePedido(models.Model):
    id_detalle_pedido = models.AutoField(primary_key=True)
    cantidad_producto = models.IntegerField()
    subtotal_detalle_pedido = models.IntegerField()
    id_producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    id_pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    estado = models.BooleanField(default=True)

    class Meta:
        db_table = 'detalle_pedido'