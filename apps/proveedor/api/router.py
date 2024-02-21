from django.urls.conf import path
from rest_framework import routers
from .ViewProveedor import ProveedorViewSet
from apps.proveedor.views import generate_pdf

urlpatterns = [
    path('proveedores/', ProveedorViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('proveedores/<int:pk>/', ProveedorViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    path('ptoveedor/generate-pdf/', generate_pdf, name='generate_pdf'),
]