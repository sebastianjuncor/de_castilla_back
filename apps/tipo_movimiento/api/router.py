from django.urls import path
from .ViewTipoMoviento import TipoMoviento

urlpatterns = [
    path('timpomovientos/', TipoMoviento.as_view({'get': 'list', 'post': 'create'})),
    path('timpomovientos/<int:pk>/', TipoMoviento.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
]