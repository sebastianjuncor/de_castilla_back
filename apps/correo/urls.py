# correo_project/urls.py

from django.urls import path
from .views import CorreoCreateView

urlpatterns = [
    path('enviar-correo/', CorreoCreateView.as_view(), name='enviar_correo'),
]
