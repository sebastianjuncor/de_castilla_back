

from django.urls import path

from .ViewClasificacion import CalificacionViewSet

urlpatterns = [
    path('clasificaciones/', CalificacionViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('clasificaciones/<int:pk>/', CalificacionViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
]