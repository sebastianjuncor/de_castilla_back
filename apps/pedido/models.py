from django.db import models
from apps.estado_pedido.models import EstadoPedido

class Pedido(models.Model):
    id_pedido = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=255)
    fecha_pedido = models.DateField()
    id_estado_pedido = models.ForeignKey(EstadoPedido, on_delete=models.CASCADE)

    class Meta:
        db_table = 'pedido'