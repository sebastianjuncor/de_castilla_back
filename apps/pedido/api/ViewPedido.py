from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from ..models import *
from rest_framework import serializers
from .PedidoSeralizers import PedidoSeralizers

class PedidoViewSet(viewsets.ModelViewSet):
    serializer_class = PedidoSeralizers  # Fix the typo in the variable name
    queryset =  PedidoSeralizers.Meta.model.objects.all()
    # permission_classes = [IsAuthenticated]