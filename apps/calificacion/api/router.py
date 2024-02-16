

from django.urls import path

from .ViewClasificacion import CalificacionViewSet

urlpatterns = [
    path('calificaciones/', CalificacionViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('calificaciones/<int:pk>/', CalificacionViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
]