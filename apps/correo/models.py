# correo_app/models.py

from django.db import models

class Correo(models.Model):
    destinatario = models.EmailField()
    asunto = models.CharField(max_length=255)
    html = models.TextField()  # Campo para el HTML del correo
