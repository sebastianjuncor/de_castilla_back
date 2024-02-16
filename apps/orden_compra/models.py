from django.db import models
from apps.estado_oc.models import EstadoOC

class OrdenCompra(models.Model):
    id_oc = models.AutoField(primary_key=True)
    fecha_oc = models.DateField()
    hora_oc = models.TimeField()
    id_estado_oc = models.ForeignKey(EstadoOC, on_delete=models.CASCADE)

    class Meta:
        db_table = 'orden_compra'