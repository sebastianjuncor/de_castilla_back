from django.urls import path
from .ViewVenta import VentaViewSet
from apps.venta.views import generate_pdf


urlpatterns = [
    path('ventas/', VentaViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('ventas/<int:pk>/', VentaViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    path('venta/generate-pdf/', generate_pdf, name='generate_pdf'),
]
