from rest_framework import serializers
from ..models import *
from rest_framework import serializers




class TipoMovientoSeralizer (serializers.ModelSerializer):
    class Meta:
        model = TipoMovimiento
        fields = '__all__'  # Incluir todos los campos del modelo