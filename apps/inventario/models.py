from django.db import models
from apps.insumo.models import Insumo
from apps.producto.models import Producto

class Inventario(models.Model):
    id_inventario = models.AutoField(primary_key=True)
    stock_inventario = models.IntegerField()
    tipo_inventario = models.CharField(max_length=255)
    id_insumo_fk = models.ForeignKey(Insumo,db_column='id_insumo_fk', on_delete=models.CASCADE, null=True, blank=True)
    id_producto_fk = models.ForeignKey(Producto,db_column='id_producto_fk', on_delete=models.CASCADE, null=True, blank=True)
    estado = models.BooleanField(default=True)

    class Meta:
        db_table = 'inventario'