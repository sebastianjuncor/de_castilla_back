from rest_framework import serializers
from ..models import *
from rest_framework import serializers




class OcHasProvedorSeralizers(serializers.ModelSerializer):
    class Meta:
        model = OCHasProveedor
        fields = '__all__'  # Incluir todos los campos del modelo