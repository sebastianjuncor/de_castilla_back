from ..models import *
from rest_framework import serializers




class CalificacionSeralizers(serializers.ModelSerializer):
    class Meta:
        model = Calificacion
        fields = '__all__'  # Incluir todos los campos del modelo