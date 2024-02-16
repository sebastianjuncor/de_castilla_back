
from django.urls import path
from .ViewDetalleOc import DetalleOCViewSet


urlpatterns = [
    path('detalleocs/', DetalleOCViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('detalleocs/<int:pk>/', DetalleOCViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
]