from rest_framework import serializers

from ..models import *
from rest_framework import serializers
from apps.pedido.api.PedidoSeralizers import PedidoSeralizers
from apps.rol.api.RoleSeralizers import RolSeralizers




class RolHasPermisosSeralizers(serializers.ModelSerializer):
    permiso = PedidoSeralizers(source='id_permiso_fk', read_only=True) # Relación muchos a uno con Permiso
    rol = RolSeralizers(source='id_rol_fk', read_only=True) # Relación muchos a uno con Rol
    class Meta:
        model = RolHasPermiso
        fields = '__all__'  # Incluir todos los campos del modelo