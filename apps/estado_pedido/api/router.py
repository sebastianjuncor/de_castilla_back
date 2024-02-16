
from django.urls import path

from .ViewEstadoPedido import EstadoPedidoViewSet



urlpatterns = [
    path('estadopedidos/', EstadoPedidoViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('estadopedidos/<int:pk>/', EstadoPedidoViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
]