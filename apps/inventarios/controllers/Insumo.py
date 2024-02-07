from rest_framework import viewsets
from ..models import Insumo
from ..serializers import InsumoSerializer

class InsumoCRUD(viewsets.ModelViewSet):
    queryset = Insumo.objects.all()
    serializer_class = InsumoSerializer