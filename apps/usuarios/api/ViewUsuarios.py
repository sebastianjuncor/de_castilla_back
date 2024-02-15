from rest_framework import viewsets
from ..api.UsuarioSeralizers import UsuarioSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from ..api.UsuarioSeralizers import CustomTokenObtainPairSerializer
from rest_framework.permissions import IsAuthenticated

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UsuarioSerializer
    queryset =  UsuarioSerializer.Meta.model.objects.all()
    # permission_classes = [IsAuthenticated]

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer