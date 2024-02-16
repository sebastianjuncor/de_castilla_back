from rest_framework import serializers

from ..models import *
from rest_framework import serializers
from apps.categoria.api.CategoriaSeralizers import CategoriaSeralizers




class ProductoSerializer(serializers.ModelSerializer):
    categoria = CategoriaSeralizers(source='id_categoria_fk', read_only=True)
    class Meta:
        model = Producto
        fields = '__all__'  # Incluir todos los campos del modelo