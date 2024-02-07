from rest_framework import viewsets
from ..models import EstadoOc
from ..serializers import EstadoOcSerializer

class EstadoOcCRUD(viewsets.ModelViewSet):
    queryset = EstadoOc.objects.all()
    serializer_class = EstadoOcSerializer