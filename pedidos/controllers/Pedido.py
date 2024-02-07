from rest_framework import viewsets
from ..models import Pedido
from ..serializers import PedidoSerializer

class PedidoCRUD(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer