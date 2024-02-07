from rest_framework import viewsets
from ..models import DetalleVenta
from ..serializers import DetalleVentaSerializer

class DetalleVentaCRUD(viewsets.ModelViewSet):
    queryset = DetalleVenta.objects.all()
    serializer_class = DetalleVentaSerializer