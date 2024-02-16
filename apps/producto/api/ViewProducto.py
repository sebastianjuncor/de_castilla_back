
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from ..models import *
from apps.producto.api.ProductoSeralizers import ProductoSerializer

class ProductoViewSet(viewsets.ModelViewSet):
    serializer_class = ProductoSerializer  # Fix the typo in the variable name
    queryset =  ProductoSerializer.Meta.model.objects.all()
    # permission_classes = [IsAuthenticated]