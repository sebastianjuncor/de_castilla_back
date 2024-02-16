from django.urls import path
from .ViewSabor import SaborViewSet

urlpatterns = [
    path('sabores/', SaborViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('sabores/<int:pk>/', SaborViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
]