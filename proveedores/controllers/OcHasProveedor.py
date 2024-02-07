from rest_framework import viewsets
from ..models import OcHasProveedor
from ..serializers import OcHasProveedorSerializer

class OcHasProveedorCRUD(viewsets.ModelViewSet):
    queryset = OcHasProveedor.objects.all()
    serializer_class = OcHasProveedorSerializer