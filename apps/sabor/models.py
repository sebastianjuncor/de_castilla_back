from django.db import models

class Sabor(models.Model):
    id_sabor = models.AutoField(primary_key=True)
    nombre_sabor = models.CharField(max_length=255)
    estado = models.BooleanField(default=True)

    class Meta:
        db_table = 'sabor'