from rest_framework import viewsets
from ..models import Historico
from ..serializers import HistoricoSerializer

class HistoricoCRUD(viewsets.ModelViewSet):
    queryset = Historico.objects.all()
    serializer_class = HistoricoSerializer