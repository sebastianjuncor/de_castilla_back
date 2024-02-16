from rest_framework import serializers
from ..models import *
from rest_framework import serializers




class CategoriaSeralizers(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'  # Incluir todos los campos del modelo