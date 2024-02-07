from rest_framework import viewsets
from ..models import Calificacion
from ..serializers import CalificacionSerializer

class CalificacionCRUD(viewsets.ModelViewSet):
    queryset = Calificacion.objects.all()
    serializer_class = CalificacionSerializer