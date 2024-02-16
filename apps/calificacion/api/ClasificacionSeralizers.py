from apps.proveedor.api.ProvedorSeralizers import ProveedorSeralizers
from ..models import *
from rest_framework import serializers




class CalificacionSeralizers(serializers.ModelSerializer):
    proveedor = ProveedorSeralizers(source = 'id_proveedor_fk', read_only = True)
    class Meta:
        model = Calificacion
        fields = '__all__'  # Incluir todos los campos del modelo