
from django.urls import path
from .ViewEstadoInsumo import EstadoInsumoViewSet

urlpatterns = [
    path('estadoinsumos/', EstadoInsumoViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('estadoinsumos/<int:pk>/', EstadoInsumoViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
]