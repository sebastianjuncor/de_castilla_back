from django.db import models
from apps.insumo.models import Insumo
from apps.orden_compra.models import OrdenCompra


class DetalleOC(models.Model):
    id_detalle_oc = models.AutoField(primary_key=True)
    cantidad_insumo = models.IntegerField()
    id_insumo_fk = models.ForeignKey(Insumo,db_column='id_insumo_fk', on_delete=models.CASCADE, blank=True, null=True)
    id_oc_fk = models.ForeignKey(OrdenCompra,db_column='id_oc_fk', on_delete=models.CASCADE, blank=True, null=True)
    estado = models.BooleanField(default=True)

    class Meta:
        db_table = 'detalle_oc'