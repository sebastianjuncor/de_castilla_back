from django.urls import path

from apps.detalle_pedido.views import generate_pdf
from .ViewDetallePedido import DetallePedidoViewSet



urlpatterns = [
    path('detallepedidos/',  DetallePedidoViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('detallepedidos/<int:pk>/',  DetallePedidoViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    path('detallepedidos/generate-pdf/<int:id_pedido>/',generate_pdf, name='generate_pdf'),]