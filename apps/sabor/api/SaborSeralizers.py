from rest_framework import serializers
from ..models import *
from rest_framework import serializers




class SaborSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sabor
        fields = '__all__'  # Incluir todos los campos del modelo