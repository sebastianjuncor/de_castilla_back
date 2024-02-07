from rest_framework import viewsets
from ..models import EstadoPedido
from ..serializers import EstadoPedidoSerializer

class EstadoPedidoCRUD(viewsets.ModelViewSet):
    queryset = EstadoPedido.objects.all()
    serializer_class = EstadoPedidoSerializer