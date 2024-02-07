from rest_framework import viewsets
from ..models import EstadoInsumo
from ..serializers import EstadoInsumoSerializer

class EstadoInsumoCRUD(viewsets.ModelViewSet):
    queryset = EstadoInsumo.objects.all()
    serializer_class = EstadoInsumoSerializer