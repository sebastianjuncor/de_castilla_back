from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from ..models import *
from rest_framework import serializers
from .InventarioSeralizers import InventarioSeralizers

class InventarioViewSet(viewsets.ModelViewSet):
    serializer_class = InventarioSeralizers # Fix the typo in the variable name
    queryset =  InventarioSeralizers.Meta.model.objects.all()
    permission_classes = [IsAuthenticated]