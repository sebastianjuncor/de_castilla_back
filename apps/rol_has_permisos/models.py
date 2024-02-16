from django.db import models
from apps.permiso.models import Permiso
from apps.rol.models import Rol

class RolHasPermiso(models.Model):
    id_rol_has_permiso = models.AutoField(primary_key=True)
    id_permiso_fk = models.ForeignKey(Permiso, db_column='id_permiso_fk', on_delete=models.CASCADE, blank=True, null=True)
    id_rol_fk = models.ForeignKey(Rol, db_column='id_rol_fk', on_delete=models.CASCADE, blank=True, null=True)
    estado = models.BooleanField(default=True)
    class Meta:
        db_table = 'rol_has_permiso'