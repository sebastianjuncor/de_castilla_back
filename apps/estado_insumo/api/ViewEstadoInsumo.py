
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from ..models import *
from rest_framework import serializers
from .EstadoInsumoSeralizers import EstadoInsumoSeralizers


class EstadoInsumoViewSet(viewsets.ModelViewSet):
    serializer_class = EstadoInsumoSeralizers # Fix the typo in the variable name
    queryset =  EstadoInsumoSeralizers.Meta.model.objects.all()
    # permission_classes = [IsAuthenticated]