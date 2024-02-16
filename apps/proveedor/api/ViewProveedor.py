
# Django Library
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .ProvedorSeralizers import ProveedorSeralizers

class ProveedorViewSet(viewsets.ModelViewSet):
    serializer_class = ProveedorSeralizers
    queryset =  ProveedorSeralizers.Meta.model.objects.all()
    # permission_classes = [IsAuthenticated]