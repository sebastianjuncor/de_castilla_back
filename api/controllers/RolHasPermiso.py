from rest_framework import viewsets
from ..models import RolHasPermiso
from ..serializers import RolHasPermisoSerializer
class RolHasPermisoCRUD(viewsets.ModelViewSet):
    queryset = RolHasPermiso.objects.all()
    serializer_class = RolHasPermisoSerializer