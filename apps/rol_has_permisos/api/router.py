from django.urls import path
from .ViewRolHasPermisos import RolHasPermisosViewSet



urlpatterns = [
    path('rolHaspermisos/', RolHasPermisosViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('rolHaspermisos/<int:pk>/', RolHasPermisosViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
]