from django.urls import path
from .ViewCategoria import CategoriaViewSet

urlpatterns = [
    path('categorias/', CategoriaViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('categorias/<int:pk>/', CategoriaViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
]