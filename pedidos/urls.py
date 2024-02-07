from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .controllers.DetallePedido import DetallePedidoCRUD
from .controllers.EstadoPedido import EstadoPedidoCRUD
from .controllers.Pedido import PedidoCRUD

router = DefaultRouter()
router.register(r'detalles_pedido',DetallePedidoCRUD )
router.register(r'estados_pedido',EstadoPedidoCRUD )
router.register(r'pedidos',PedidoCRUD )

urlpatterns=[
    path('',include(router.urls)),
]
