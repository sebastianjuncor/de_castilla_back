from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from ..api.RolHasPermisosSeralizers import RolHasPermisosSeralizers



class RolHasPermisosViewSet(viewsets.ModelViewSet):
    serializer_class = RolHasPermisosSeralizers
    queryset =  RolHasPermisosSeralizers.Meta.model.objects.all()
    # permission_classes = [IsAuthenticated]