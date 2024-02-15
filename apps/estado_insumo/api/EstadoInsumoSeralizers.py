from rest_framework import serializers
from ..models import *
from rest_framework import serializers




class EstadoInsumoSeralizers(serializers.ModelSerializer):
    class Meta:
        model = EstadoInsumo
        fields = '__all__'  # Incluir todos los campos del modelo