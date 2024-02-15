from django.urls import path
from .ViewInventario import InventarioViewSet

urlpatterns = [
    path('inventario/', InventarioViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('inventario/<int:pk>/', InventarioViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
]