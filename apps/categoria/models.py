from django.db import models

class Categoria(models.Model):
    id_categoria = models.AutoField(primary_key=True)
    descripcion_categoria = models.CharField(max_length=255)
    nombre_categoria = models.CharField(max_length=255)
    estado = models.BooleanField(default=True)

    class Meta:
        db_table = 'categoria'