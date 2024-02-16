


from django.urls import path

from .ViewEstadoOc import EstadoOCViewSet



urlpatterns = [
    path('estadoocs/', EstadoOCViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('estadoocs/<int:pk>/', EstadoOCViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
]