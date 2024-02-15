
from django.urls import path

from .ViewEstadoPedido import EstadoPedidoViewSet



urlpatterns = [
    path('historicos/', EstadoPedidoViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('historicos/<int:pk>/', EstadoPedidoViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
]