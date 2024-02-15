from rest_framework import viewsets
from ..api.VentaSeralizers import VentaSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import IsAuthenticated


class VentaViewSet(viewsets.ModelViewSet):
    serializer_class = VentaSerializer
    queryset =  VentaSerializer.Meta.model.objects.all()
    permission_classes = [IsAuthenticated]