


from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from ..models import *
from rest_framework import serializers
from .CategoriaSeralizers import CategoriaSeralizers



class CategoriaViewSet(viewsets.ModelViewSet):
    serializer_class =  CategoriaSeralizers # Fix the typo in the variable name
    queryset =   CategoriaSeralizers.Meta.model.objects.all()
    permission_classes = [IsAuthenticated]