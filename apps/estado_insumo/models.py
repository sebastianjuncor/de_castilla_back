from django.db import models

class EstadoInsumo(models.Model):
    id_estado_insumo = models.AutoField(primary_key=True)
    nombre_estado_insumo = models.CharField(max_length=255)
    estado = models.BooleanField(default=True)

    class Meta:
        db_table = 'estado_insumo'