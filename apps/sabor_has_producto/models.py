from django.db import models
from apps.producto.models import Producto
from apps.sabor.models import Sabor

class SaborHasProducto(models.Model):
    id_sabor_has_producto = models.AutoField(primary_key=True)
    id_producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    id_sabor = models.ForeignKey(Sabor, on_delete=models.CASCADE)
    estado = models.BooleanField(default=True)

    class Meta:
        db_table = 'sabor_has_producto'