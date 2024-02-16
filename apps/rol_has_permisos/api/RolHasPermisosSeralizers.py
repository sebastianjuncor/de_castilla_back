from rest_framework import serializers
from ..models import *
from rest_framework import serializers




class RolHasPermisosSeralizers(serializers.ModelSerializer):
    class Meta:
        model = RolHasPermiso
        fields = '__all__'  # Incluir todos los campos del modelo