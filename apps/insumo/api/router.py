from django.urls import path
from .ViewInsumo import InsumoViewSet


urlpatterns = [
    path('insumos/', InsumoViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('insumos/<int:pk>/', InsumoViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
]