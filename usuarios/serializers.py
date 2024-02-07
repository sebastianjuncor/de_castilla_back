from rest_framework import serializers

from .models import *

class RolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rol
        fields = '__all__'

class PermisoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permiso
        fields = '__all__'

class UsuarioSerializer(serializers.ModelSerializer):
    rol = RolSerializer(source = 'id_rol_fk', read_only = True)
    class Meta:
        model = Usuario
        fields = '__all__'

class RolHasPermisoSerializer(serializers.ModelSerializer):
    permiso = PermisoSerializer(source = 'id_permiso_fk', read_only = True)
    rol = RolSerializer(source = 'id_rol_fk', read_only = True)
    class Meta:
        model = RolHasPermiso
        fields = '__all__'
