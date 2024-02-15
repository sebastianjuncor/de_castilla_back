from django.urls.conf import path
from rest_framework import routers
from .ViewProveedor import ProveedorViewSet

urlpatterns = [
    path('proveedores/', ProveedorViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('proveedores/<int:pk>/', ProveedorViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
]