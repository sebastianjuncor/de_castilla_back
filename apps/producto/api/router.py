from django.urls import path
from .ViewProducto import ProductoViewSet



urlpatterns = [
    path('productos/', ProductoViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('productos/<int:pk>/', ProductoViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
]