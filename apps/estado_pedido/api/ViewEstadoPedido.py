

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from ..models import *
from rest_framework import serializers
from .EstadoPedidoSeralizers import  EstadoPedidoSeralizers

class EstadoPedidoViewSet(viewsets.ModelViewSet):
    serializer_class = EstadoPedidoSeralizers # Fix the typo in the variable name
    queryset =  EstadoPedidoSeralizers.Meta.model.objects.all()
    # permission_classes = [IsAuthenticated]