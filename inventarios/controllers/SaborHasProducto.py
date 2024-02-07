from rest_framework import viewsets
from ..models import SaborHasProducto
from ..serializers import SaborHasProductoSerializer

class SaborHasProductoCRUD(viewsets.ModelViewSet):
    queryset = SaborHasProducto.objects.all()
    serializer_class = SaborHasProductoSerializer