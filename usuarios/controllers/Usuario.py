from rest_framework import viewsets
from ..models import Usuario
from ..serializers import UsuarioSerializer

class UsuarioCRUD(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer