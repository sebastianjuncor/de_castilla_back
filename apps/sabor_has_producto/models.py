from django.db import models
from apps.producto.models import Producto
from apps.sabor.models import Sabor

class SaborHasProducto(models.Model):
    id_sabor_has_producto = models.AutoField(primary_key=True)
    id_producto_fk = models.ForeignKey(Producto, db_column='id_producto_fk', on_delete=models.CASCADE, blank=True, null=True)
    id_sabor_fk = models.ForeignKey(Sabor, db_column='id_sabor_fk', on_delete=models.CASCADE, blank=True, null=True)
    estado = models.BooleanField(default=True)

    class Meta:
        db_table = 'sabor_has_producto'