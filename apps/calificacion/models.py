from django.db import models
from apps.proveedor.models import Proveedor

class Calificacion(models.Model):
    id_calificacion = models.AutoField(primary_key=True)
    comentario_calificacion = models.TextField()
    estrellas_calificacion = models.IntegerField()
    id_proveedor_fk = models.ForeignKey(Proveedor,db_column='id_proveedor_fk', on_delete=models.CASCADE, blank=True, null=True)
    estado = models.BooleanField(default=True)

    class Meta:
        db_table = 'calificacion'