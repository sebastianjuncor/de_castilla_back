from rest_framework import serializers
from ..models import *
from rest_framework import serializers




class DetalleOCSeralizers(serializers.ModelSerializer):
    class Meta:
        model = DetalleOC
        fields = '__all__'  # Incluir todos los campos del modelo