from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from ..api.SaborSeralizers import SaborSerializer

class SaborViewSet(viewsets.ModelViewSet):
    serializer_class = SaborSerializer
    queryset =  SaborSerializer.Meta.model.objects.all()
    # permission_classes = [IsAuthenticated]