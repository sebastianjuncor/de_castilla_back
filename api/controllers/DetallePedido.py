from rest_framework import viewsets
from ..models import DetallePedido
from ..serializers import DetallePedidoSerializer

class DetallePedidoCRUD(viewsets.ModelViewSet):
    queryset = DetallePedido.objects.all()
    serializer_class = DetallePedidoSerializer