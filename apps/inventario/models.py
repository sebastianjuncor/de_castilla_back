from django.db import models
from apps.insumo.models import Insumo
from apps.producto.models import Producto

class Inventario(models.Model):
    id_inventario = models.AutoField(primary_key=True)
    stock_inventario = models.IntegerField()
    tipo_inventario = models.CharField(max_length=255)
    id_insumo = models.ForeignKey(Insumo, on_delete=models.CASCADE, null=True)
    id_producto = models.ForeignKey(Producto, on_delete=models.CASCADE, null=True)
    estado = models.BooleanField(default=True)

    class Meta:
        db_table = 'inventario'