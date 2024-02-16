from django.db import models
from apps.orden_compra.models import OrdenCompra
from apps.proveedor.models import Proveedor

class OCHasProveedor(models.Model):
    id_has_proveedor = models.AutoField(primary_key=True)
    id_oc_fk = models.ForeignKey(OrdenCompra, db_column='id_oc_fk', on_delete=models.CASCADE, null=True, blank=True)
    id_proveedor_fk = models.ForeignKey(Proveedor, db_column='id_proveedor_fk', on_delete=models.CASCADE, null=True, blank=True)
    estado = models.BooleanField(default=True)

    class Meta:
        db_table = 'oc_has_proveedor'