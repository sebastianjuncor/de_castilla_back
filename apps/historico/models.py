from django.db import models
from apps.insumo.models import Insumo
from apps.producto.models import Producto
from apps.tipo_movimiento.models import TipoMovimiento

class Historico(models.Model):
    id_historico = models.AutoField(primary_key=True)
    cantidad_historico = models.IntegerField()
    fecha_caducidad = models.DateField(null=True, blank=True)
    fecha_movimiento = models.DateField()
    tipo_historico = models.CharField(max_length=255)
    id_insumo_fk = models.ForeignKey(Insumo, db_column='id_insumo_fk', on_delete=models.CASCADE, null=True, blank=True)
    id_producto_fk = models.ForeignKey(Producto, db_column='id_producto_fk', on_delete=models.CASCADE, null=True, blank=True)
    id_tipo_movimiento_fk = models.ForeignKey(TipoMovimiento, db_column='id_tipo_movimiento_fk', on_delete=models.CASCADE, null=True, blank=True)
    estado = models.BooleanField(default=True)

    class Meta:
        db_table = 'historico'