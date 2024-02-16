

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from ..models import *
from rest_framework import serializers
from .EstadoOcSeralizers import  EstadoOCSeralizers

class EstadoOCViewSet(viewsets.ModelViewSet):
    serializer_class = EstadoOCSeralizers # Fix the typo in the variable name
    queryset =  EstadoOCSeralizers.Meta.model.objects.all()
    permission_classes = [IsAuthenticated]