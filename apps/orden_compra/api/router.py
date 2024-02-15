
# Django REST Framework
from rest_framework.routers import DefaultRouter
from django.urls import path
from .ViewOrdenCompra import OrdenCompraViewSet


urlpatterns = [
    path('ordencompras/', OrdenCompraViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('ordencompras/<int:pk>/', OrdenCompraViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
]