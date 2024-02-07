from django.db import models

from inventarios.models import Insumo

class Calificacion(models.Model):
    id_calificacion = models.BigAutoField(primary_key=True)
    comentario_calificacion = models.CharField(max_length=255, blank=True, null=True)
    estrallas_calificacion = models.IntegerField(blank=True, null=True)
    id_proveedor_fk = models.ForeignKey('Proveedor', models.DO_NOTHING, db_column='id_proveedor_fk', blank=True, null=True)
    estado = models.BooleanField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'calificacion'

class EstadoOc(models.Model):
    id_estado_oc = models.BigAutoField(primary_key=True)
    nombre_estado_oc = models.CharField(max_length=255, blank=True, null=True)
    estado = models.BooleanField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'estado_oc'

class OrdenCompra(models.Model):
    id_oc = models.BigAutoField(primary_key=True)
    fecha_oc = models.DateField(blank=True, null=True)
    hora_oc = models.TimeField(blank=True, null=True)
    id_estado_oc_fk = models.ForeignKey(EstadoOc, models.DO_NOTHING, db_column='id_estado_oc_fk', blank=True, null=True)
    estado = models.BooleanField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'orden_compra'

class DetalleOc(models.Model):
    id_detalle_oc = models.BigAutoField(primary_key=True)
    cantidad_insumo = models.IntegerField(blank=True, null=True)
    id_insumo_fk = models.ForeignKey(Insumo, models.DO_NOTHING, db_column='id_insumo_fk', blank=True, null=True)
    id_oc_fk = models.ForeignKey(OrdenCompra, models.DO_NOTHING, db_column='id_oc_fk', blank=True, null=True)
    estado = models.BooleanField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'detalle_oc'

class Proveedor(models.Model):
    id_proveedor = models.BigAutoField(primary_key=True)
    celular_proveedor = models.BigIntegerField(blank=True, null=True)
    celular_respaldo_proveedor = models.BigIntegerField(blank=True, null=True)
    correo_proveedor = models.CharField(max_length=255, blank=True, null=True)
    empresa_proveedor = models.CharField(max_length=255, blank=True, null=True)
    estado_proveedor = models.BooleanField() # This field type is a guess.
    nit_proveedor = models.BigIntegerField(blank=True, null=True)
    nombre_proveedor = models.CharField(max_length=255, blank=True, null=True)
    estado = models.BooleanField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'proveedor'

class OcHasProveedor(models.Model):
    id_oc_has_proveedor = models.BigAutoField(primary_key=True)
    id_oc_fk = models.ForeignKey(OrdenCompra, models.DO_NOTHING, db_column='id_oc_fk', blank=True, null=True)
    id_proveedor_fk = models.ForeignKey(Proveedor, models.DO_NOTHING, db_column='id_proveedor_fk', blank=True, null=True)
    estado = models.BooleanField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'oc_has_proveedor'
