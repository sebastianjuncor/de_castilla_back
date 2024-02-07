from rest_framework import viewsets
from ..models import Permiso
from ..serializers import PermisoSerializer

class PermisoCRUD(viewsets.ModelViewSet):
    queryset = Permiso.objects.all()
    serializer_class = PermisoSerializer
