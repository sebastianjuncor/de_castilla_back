from django.db import models
from apps.insumo.models import Insumo
from apps.producto.models import Producto
from apps.tipo_movimiento.models import TipoMovimiento

class Historico(models.Model):
    id_historico = models.AutoField(primary_key=True)
    cantidad_historico = models.IntegerField()
    fecha_caducidad = models.DateField()
    fecha_movimiento = models.DateField()
    tipo_historico = models.CharField(max_length=255)
    id_insumo = models.ForeignKey(Insumo, on_delete=models.CASCADE)
    id_producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    id_tipo_movimiento = models.ForeignKey(TipoMovimiento, on_delete=models.CASCADE)
    estado = models.BooleanField(default=True)

    class Meta:
        db_table = 'historico'