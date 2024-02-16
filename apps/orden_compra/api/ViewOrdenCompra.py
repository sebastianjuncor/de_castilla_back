from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from ..models import *
from rest_framework import serializers
from .OrdenCompraSeralizers import OrdenCompraSeralizers

class OrdenCompraViewSet(viewsets.ModelViewSet):
    serializer_class = OrdenCompraSeralizers # Fix the typo in the variable name
    queryset =  OrdenCompraSeralizers.Meta.model.objects.all()
    # permission_classes = [IsAuthenticated]