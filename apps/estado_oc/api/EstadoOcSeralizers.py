from rest_framework import serializers
from ..models import *
from rest_framework import serializers




class EstadoOCSeralizers(serializers.ModelSerializer):
    class Meta:
        model = EstadoOC
        fields = '__all__'  # Incluir todos los campos del modelo