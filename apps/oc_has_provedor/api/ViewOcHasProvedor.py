from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from ..models import *
from rest_framework import serializers
from .OcHasProvedorSeralizers import OcHasProvedorSeralizers

class OcHasProvedorViewSet(viewsets.ModelViewSet):
    serializer_class = OcHasProvedorSeralizers # Fix the typo in the variable name
    queryset =  OcHasProvedorSeralizers.Meta.model.objects.all()
    permission_classes = [IsAuthenticated]