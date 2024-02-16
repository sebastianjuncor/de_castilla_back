from django.db import models
from apps.pedido.models import Pedido
from apps.usuarios.models import Usuario

class Venta(models.Model):
    id_venta = models.AutoField(primary_key=True)
    fecha_venta = models.DateField()
    hora_venta = models.TimeField()
    total_venta = models.IntegerField()
    id_pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    no_documento_usuario_fk = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    estado = models.BooleanField(default=True)

    class Meta:
        db_table = 'venta'