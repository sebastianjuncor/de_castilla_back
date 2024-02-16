from django.urls import path
from .ViewDetallePedido import DetallePedidoViewSet



urlpatterns = [
    path('detallepedidos/',  DetallePedidoViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('detallepedidos/<int:pk>/',  DetallePedidoViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
]