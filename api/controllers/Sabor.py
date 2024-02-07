from rest_framework import viewsets
from ..models import Sabor
from ..serializers import SaborSerializer

class SaborCRUD(viewsets.ModelViewSet):
    queryset = Sabor.objects.all()
    serializer_class = SaborSerializer