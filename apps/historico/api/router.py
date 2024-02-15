from django.urls import path
from .ViewHistorico import HistoricoViewSet


urlpatterns = [
    path('historicos/', HistoricoViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('historicos/<int:pk>/', HistoricoViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
]