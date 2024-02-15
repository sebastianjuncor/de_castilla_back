
# Django REST Framework
from rest_framework import routers
from django.urls import path
from .ViewPedido import PedidoViewSet


urlpatterns = [
    path('pedidos/', PedidoViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('pedidos/<int:pk>/', PedidoViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
]