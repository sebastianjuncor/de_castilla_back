from rest_framework import viewsets
from ..models import Proveedor
from ..serializers import ProveedorSerializer

class ProveedorCRUD(viewsets.ModelViewSet):
    queryset = Proveedor.objects.all()
    serializer_class = ProveedorSerializer