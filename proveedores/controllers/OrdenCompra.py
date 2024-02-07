from rest_framework import viewsets
from ..models import OrdenCompra
from ..serializers import OrdenCompraSerializer

class OrdenCompraCRUD(viewsets.ModelViewSet):
    queryset = OrdenCompra.objects.all()
    serializer_class = OrdenCompraSerializer