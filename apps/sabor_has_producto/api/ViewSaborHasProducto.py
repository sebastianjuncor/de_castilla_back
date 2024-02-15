from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from ..api.SaborHasProductoSeralizers import SaborHasProductoSeralizer



class SaborHasProducto(viewsets.ModelViewSet):
    serializer_class = SaborHasProductoSeralizer
    queryset =  SaborHasProductoSeralizer.Meta.model.objects.all()
    permission_classes = [IsAuthenticated]