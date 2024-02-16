

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from ..models import *
from rest_framework import serializers
from .DetalleOcSeralizers import DetalleOCSeralizers



class DetalleOCViewSet(viewsets.ModelViewSet):
    serializer_class =  DetalleOCSeralizers # Fix the typo in the variable name
    queryset =   DetalleOCSeralizers.Meta.model.objects.all()
    permission_classes = [IsAuthenticated]