





from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from ..models import *
from rest_framework import serializers
from .ClasificacionSeralizers import CalificacionSeralizers



class CalificacionViewSet(viewsets.ModelViewSet):
    serializer_class =  CalificacionSeralizers # Fix the typo in the variable name
    queryset =   CalificacionSeralizers.Meta.model.objects.all()
    permission_classes = [IsAuthenticated]