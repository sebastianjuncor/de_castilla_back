from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .controllers.DetalleVenta import DetalleVentaCRUD
from .controllers.Venta import VentaCRUD

router = DefaultRouter()
router.register(r'detalles_venta',DetalleVentaCRUD )
router.register(r'ventas',VentaCRUD )


urlpatterns=[
    path('',include(router.urls)),
]