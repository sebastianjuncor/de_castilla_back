from rest_framework import viewsets
from ..models import Usuario
from ..serializers import UsuarioSerializer

from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.contrib.auth.hashers import make_password

@receiver(pre_save, sender = Usuario)
def encriptar_contrasena(sender, instance, **kwargs):
    if instance.password:
        instance.password = make_password(instance.password)

class UsuarioCRUD(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer