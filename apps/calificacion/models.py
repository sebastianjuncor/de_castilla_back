from django.db import models
from apps.proveedor.models import Proveedor

class Calificacion(models.Model):
    id_calificacion = models.AutoField(primary_key=True)
    comentario_calificacion = models.TextField()
    estrellas_calificacion = models.IntegerField()
    id_proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    estado = models.BooleanField(default=True)

    class Meta:
        db_table = 'calificacion'