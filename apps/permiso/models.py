from django.db import models

class Permiso(models.Model):
    id_permiso = models.AutoField(primary_key=True)
    description_permiso = models.CharField(max_length=255)
    estado = models.BooleanField(default=True)

    class Meta:
        db_table = 'permiso'