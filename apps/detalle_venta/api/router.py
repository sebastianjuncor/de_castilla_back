
from django.urls import path
from .ViewDetalleVenta import DetalleVentaViewSet



urlpatterns = [
    path('detalleventas/', DetalleVentaViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('detalleventas/<int:pk>/', DetalleVentaViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
]