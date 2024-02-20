# correo_app/serializers.py

from rest_framework import serializers
from .models import Correo

class CorreoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Correo
        fields = ['destinatario', 'asunto', 'html']  # Asegúrate de incluir 'html'
