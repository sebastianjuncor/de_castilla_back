from rest_framework import serializers
from ..models import *
from rest_framework import serializers




class SaborHasProductoSeralizer(serializers.ModelSerializer):
    class Meta:
        model = SaborHasProducto
        fields = '__all__'  # Incluir todos los campos del modelo