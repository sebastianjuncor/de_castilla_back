from django.db import models

class EstadoOC(models.Model):
    id_estado_oc = models.AutoField(primary_key=True)
    nombre_estado_oc = models.CharField(max_length=255)
    estado = models.BooleanField(default=True)

    class Meta:
        db_table = 'estado_oc'