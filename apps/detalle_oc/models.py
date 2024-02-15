from django.db import models
from apps.insumo.models import Insumo
from apps.estado_oc.models import EstadoOC


class DetalleOC(models.Model):
    id_detalle_oc = models.AutoField(primary_key=True)
    cantidad_insumo = models.IntegerField()
    id_insumo = models.ForeignKey(Insumo, on_delete=models.CASCADE)
    id_oc = models.ForeignKey(EstadoOC, on_delete=models.CASCADE)
    estado = models.BooleanField(default=True)

    class Meta:
        db_table = 'detalle_oc'