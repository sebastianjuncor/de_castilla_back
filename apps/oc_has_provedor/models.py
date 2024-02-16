from django.db import models
from apps.orden_compra.models import OrdenCompra

class OCHasProveedor(models.Model):
    id_has_proveedor = models.AutoField(primary_key=True)
    id_oc = models.ForeignKey(OrdenCompra, on_delete=models.CASCADE)
    estado = models.BooleanField(default=True)

    class Meta:
        db_table = 'oc_has_proveedor'