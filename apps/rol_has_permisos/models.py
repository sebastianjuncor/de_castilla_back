from django.db import models
from apps.permiso.models import Permiso
from apps.rol.models import Rol

class RolHasPermiso(models.Model):
    id_rol_has_permiso = models.AutoField(primary_key=True)
    id_permiso = models.ForeignKey(Permiso, on_delete=models.CASCADE)
    id_rol = models.ForeignKey(Rol, on_delete=models.CASCADE)

    class Meta:
        db_table = 'rol_has_permiso'