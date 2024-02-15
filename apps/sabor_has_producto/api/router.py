from django.urls import path
from .ViewSaborHasProducto import SaborHasProducto

urlpatterns = [
    path('saborhasproductos/', SaborHasProducto.as_view({'get': 'list', 'post': 'create'})),
    path('saborhasproductos/<int:pk>/', SaborHasProducto.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
]