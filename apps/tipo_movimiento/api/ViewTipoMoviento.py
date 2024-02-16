from rest_framework import viewsets
from ..api.TipoMovientoSeralizers import TipoMovientoSeralizer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import IsAuthenticated


class TipoMoviento(viewsets.ModelViewSet):
    serializer_class = TipoMovientoSeralizer
    queryset =  TipoMovientoSeralizer.Meta.model.objects.all()
    # permission_classes = [IsAuthenticated]