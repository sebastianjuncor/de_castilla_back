

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from ..models import *
from rest_framework import serializers
from .PermisoSeralizers import PrermisoSeralizers

class PermisoViewSet(viewsets.ModelViewSet):
    serializer_class = PrermisoSeralizers  # Fix the typo in the variable name
    queryset =  PrermisoSeralizers.Meta.model.objects.all()
    permission_classes = [IsAuthenticated]