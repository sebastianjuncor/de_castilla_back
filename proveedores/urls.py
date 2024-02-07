from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .controllers.Calificacion import CalificacionCRUD
from .controllers.DetalleOc import DetalleOcCRUD
from .controllers.EstadoOc import EstadoOcCRUD
from .controllers.OcHasProveedor import OcHasProveedorCRUD
from .controllers.OrdenCompra import OrdenCompraCRUD
from .controllers.Proveedor import ProveedorCRUD

router = DefaultRouter()
router.register(r'calificaciones',CalificacionCRUD )
router.register(r'detalles_oc',DetalleOcCRUD )
router.register(r'estados_oc',EstadoOcCRUD )
router.register(r'oc_has_roveedor',OcHasProveedorCRUD )
router.register(r'ordenes_compra',OrdenCompraCRUD )
router.register(r'proveedores',ProveedorCRUD )


urlpatterns=[
    path('',include(router.urls)),
]