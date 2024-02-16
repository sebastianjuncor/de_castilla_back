from django.urls.conf import path
from rest_framework import routers
from .ViewRole import RolViewSet

urlpatterns = [
    path('roles/', RolViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('roles/<int:pk>/', RolViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
]