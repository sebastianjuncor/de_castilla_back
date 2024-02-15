from django.db import models

class EstadoPedido(models.Model):
    id_estado_pedido = models.AutoField(primary_key=True)
    nombre_estado = models.CharField(max_length=255)
    estado = models.BooleanField(default=True)

    class Meta:
        db_table = 'estado_pedido'