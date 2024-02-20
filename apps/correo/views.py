# correo_app/views.py

from rest_framework import generics
from .models import Correo
from .serializers import CorreoSerializer
from django.core.mail import send_mail
from django.conf import settings

class CorreoCreateView(generics.CreateAPIView):
    queryset = Correo.objects.all()
    serializer_class = CorreoSerializer

    def create(self, request, *args, **kwargs):
        destinatario = request.data.get('destinatario', '')
        asunto = request.data.get('asunto', '')
        html = request.data.get('html', '')

        send_mail(
            asunto,
            '',
            settings.EMAIL_HOST_USER,
            [destinatario],
            html_message=html,
        )
        return super().create(request, *args, **kwargs)
