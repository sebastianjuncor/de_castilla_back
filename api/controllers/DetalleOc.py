from rest_framework import viewsets
from ..models import DetalleOc
from ..serializers import DetalleOcSerializer

class DetalleOcCRUD(viewsets.ModelViewSet):
    queryset = DetalleOc.objects.all()
    serializer_class = DetalleOcSerializer