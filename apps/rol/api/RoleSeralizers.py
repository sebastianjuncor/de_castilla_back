from rest_framework import serializers
from ..models import *
from rest_framework import serializers




class RolSeralizers(serializers.ModelSerializer):
    class Meta:
        model = Rol
        fields = '__all__'  # Incluir todos los campos del modelo