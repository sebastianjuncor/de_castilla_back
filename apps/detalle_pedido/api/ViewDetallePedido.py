
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse
from ..models import *
from rest_framework import serializers
from rest_framework import generics

from apps.detalle_pedido.api.DetallePedidoSeralizers import DetallePedidoSeralizers


class DetallePedidoViewSet(viewsets.ModelViewSet):
    serializer_class =  DetallePedidoSeralizers # Fix the typo in the variable name
    queryset =   DetallePedidoSeralizers.Meta.model.objects.all()
    # permission_classes = [IsAuthenticated]


class DetallesPedidoView(generics.ListAPIView):
    serializer_class = DetallePedidoSeralizers  # Asegúrate de importar el serializador adecuado
    queryset = DetallePedido.objects.all()  # Define el queryset inicial

    def get_queryset(self):
        id_pedido_fk = self.kwargs['id_pedido_fk']
        return DetallePedido.objects.filter(id_pedido_fk=id_pedido_fk)