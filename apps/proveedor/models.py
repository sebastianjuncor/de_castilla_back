from django.db import models

class Proveedor(models.Model):
    id_proveedor = models.AutoField(primary_key=True)
    celular_proveedor = models.CharField(max_length=20)
    correo_proveedor = models.EmailField(max_length=255)
    celular_respaldo_proveedor = models.CharField(max_length=20)
    empresa_proveedor = models.CharField(max_length=255)
    estado_proveedor = models.BooleanField(default=True)
    nit_proveedor = models.CharField(max_length=20)
    nombre_proveedor = models.CharField(max_length=255)
    estado = models.BooleanField(default=True)

    class Meta:
        db_table = 'proveedor'