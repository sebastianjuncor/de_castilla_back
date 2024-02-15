
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from ..models import *
from rest_framework import serializers

from apps.detalle_pedido.api.DetallePedidoSeralizers import DetallePedidoSeralizers


class DetallePedidoViewSet(viewsets.ModelViewSet):
    serializer_class =  DetallePedidoSeralizers # Fix the typo in the variable name
    queryset =   DetallePedidoSeralizers.Meta.model.objects.all()
    permission_classes = [IsAuthenticated]