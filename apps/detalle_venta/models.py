from django.db import models
from apps.venta.models import Venta
from apps.producto.models import Producto

class DetalleVenta(models.Model):
    id_detalle_venta = models.AutoField(primary_key=True)
    cantidad_producto = models.IntegerField()
    subtotal_detalle_venta = models.IntegerField()
    id_producto_fk = models.ForeignKey(Producto, db_column='id_producto_fk', on_delete=models.CASCADE, blank=True, null=True)
    id_venta_fk = models.ForeignKey(Venta, db_column='id_venta_fk', on_delete=models.CASCADE, blank=True, null=True)
    estado = models.BooleanField(default=True)

    class Meta:
        db_table = 'detalle_venta'