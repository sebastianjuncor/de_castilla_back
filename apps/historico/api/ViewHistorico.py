

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from ..models import *
from rest_framework import serializers
from .HistoricoSeralizers import  HistoricoSeralizers

class HistoricoViewSet(viewsets.ModelViewSet):
    serializer_class = HistoricoSeralizers # Fix the typo in the variable name
    queryset =  HistoricoSeralizers.Meta.model.objects.all()
    permission_classes = [IsAuthenticated]