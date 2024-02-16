from django.urls import path
from .ViewVenta import VentaViewSet


urlpatterns = [
    path('ventas/', VentaViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('ventas/<int:pk>/', VentaViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
]