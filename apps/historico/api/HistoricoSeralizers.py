from rest_framework import serializers
from ..models import *
from rest_framework import serializers




class HistoricoSeralizers(serializers.ModelSerializer):
    class Meta:
        model = Historico
        fields = '__all__'  # Incluir todos los campos del modelo