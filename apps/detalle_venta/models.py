from django.db import models
from apps.venta.models import Venta
from apps.producto.models import Producto

class DetalleVenta(models.Model):
    id_detalle_venta = models.AutoField(primary_key=True)
    cantidad_producto = models.IntegerField()
    subtotal_detalle_venta = models.IntegerField()
    id_producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    id_venta = models.ForeignKey(Venta, on_delete=models.CASCADE)
    estado = models.BooleanField(default=True)

    class Meta:
        db_table = 'detalle_venta'