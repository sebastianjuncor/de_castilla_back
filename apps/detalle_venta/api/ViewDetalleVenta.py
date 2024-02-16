

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from ..models import *
from rest_framework import serializers
from .DetalleVentaSeralizers import DetalleVentaSeralizers



class DetalleVentaViewSet(viewsets.ModelViewSet):
    serializer_class = DetalleVentaSeralizers # Fix the typo in the variable name
    queryset =  DetalleVentaSeralizers.Meta.model.objects.all()
    # permission_classes = [IsAuthenticated]