from django.db import models

# Create your models here.
class Permiso(models.Model):
    id_permiso = models.BigAutoField(primary_key=True)
    descripcion_permiso = models.CharField(max_length=255, blank=True, null=True)
    estado = models.BooleanField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'permiso'

class Rol(models.Model):
    id_rol = models.BigAutoField(primary_key=True)
    nombre_rol = models.CharField(max_length=255, blank=True, null=True)
    estado = models.BooleanField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'rol'

class RolHasPermiso(models.Model):
    id_rol_has_permiso = models.BigAutoField(primary_key=True)
    id_permiso_fk = models.ForeignKey(Permiso, models.DO_NOTHING, db_column='id_permiso_fk', blank=True, null=True)
    id_rol_fk = models.ForeignKey(Rol, models.DO_NOTHING, db_column='id_rol_fk', blank=True, null=True)
    estado = models.BooleanField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'rol_has_permiso'

class Usuario(models.Model):
    no_documento_usuario = models.BigAutoField(primary_key=True)
    apellido_usuario = models.CharField(max_length=255, blank=True, null=True)
    celular_usuario = models.BigIntegerField(blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    nombre_usuario = models.CharField(max_length=255, blank=True, null=True)
    password = models.CharField(max_length=255, blank=True, null=True)
    id_rol_fk = models.ForeignKey(Rol, models.DO_NOTHING, db_column='id_rol_fk', blank=True, null=True)
    estado = models.BooleanField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'usuario'
