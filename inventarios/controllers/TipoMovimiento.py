from rest_framework import viewsets
from ..models import TipoMovimiento
from ..serializers import TipoMovimientoSerializer

class TipoMovimientoCRUD(viewsets.ModelViewSet):
    queryset = TipoMovimiento.objects.all()
    serializer_class = TipoMovimientoSerializer