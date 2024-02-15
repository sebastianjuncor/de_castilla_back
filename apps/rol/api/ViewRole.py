
# Django
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .RoleSeralizers import RolSeralizers


class RolViewSet(viewsets.ModelViewSet):
    serializer_class = RolSeralizers
    queryset =  RolSeralizers.Meta.model.objects.all()
    permission_classes = [IsAuthenticated]