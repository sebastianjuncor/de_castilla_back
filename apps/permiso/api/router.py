
# Django
from django.urls import path
from rest_framework import routers

# View
from .ViewPermiso import PermisoViewSet

urlpatterns = [
    path('permisos/', PermisoViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('permisos/<int:pk>/', PermisoViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
]