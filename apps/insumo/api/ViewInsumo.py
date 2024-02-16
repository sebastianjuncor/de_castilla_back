from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from ..models import *
from rest_framework import serializers
from .InsumoSeralizers import  InsumoSeralizers

class InsumoViewSet(viewsets.ModelViewSet):
    serializer_class = InsumoSeralizers # Fix the typo in the variable name
    queryset =  InsumoSeralizers.Meta.model.objects.all()
    # permission_classes = [IsAuthenticated]