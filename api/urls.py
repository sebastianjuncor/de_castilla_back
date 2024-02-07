from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .controllers.Calificacion import CalificacionCRUD
from .controllers.Categoria import CategoriaCRUD
from .controllers.DetalleOc import DetalleOcCRUD
from .controllers.DetallePedido import DetallePedidoCRUD
from .controllers.DetalleVenta import DetalleVentaCRUD
from .controllers.EstadoInsumo import EstadoInsumoCRUD
from .controllers.EstadoOc import EstadoOcCRUD
from .controllers.EstadoPedido import EstadoPedidoCRUD
from .controllers.Historico import HistoricoCRUD
from .controllers.Insumo import InsumoCRUD
from .controllers.Inventario import InventarioCRUD
from .controllers.OcHasProveedor import OcHasProveedorCRUD
from .controllers.OrdenCompra import OrdenCompraCRUD
from .controllers.Pedido import PedidoCRUD
from .controllers.Permiso import PermisoCRUD
from .controllers.Producto import ProductoCRUD
from .controllers.Proveedor import ProveedorCRUD
from .controllers.Rol import RolCRUD
from .controllers.RolHasPermiso import RolHasPermisoCRUD
from .controllers.Sabor import SaborCRUD
from .controllers.SaborHasProducto import SaborHasProductoCRUD
from .controllers.TipoMovimiento import TipoMovimientoCRUD
from .controllers.Usuario import UsuarioCRUD
from .controllers.Venta import VentaCRUD

router = DefaultRouter()
router.register(r'Calificacion',CalificacionCRUD )
router.register(r'Categoria',CategoriaCRUD )
router.register(r'DetalleOc',DetalleOcCRUD )
router.register(r'DetallePedido',DetallePedidoCRUD )
router.register(r'DetalleVenta',DetalleVentaCRUD )
router.register(r'EstadoInsumo',EstadoInsumoCRUD )
router.register(r'EstadoOc',EstadoOcCRUD )
router.register(r'EstadoPedido',EstadoPedidoCRUD )
router.register(r'Historico',HistoricoCRUD )
router.register(r'Insumo',InsumoCRUD )
router.register(r'Inventario',InventarioCRUD )
router.register(r'OcHasProveedor',OcHasProveedorCRUD )
router.register(r'OrdenCompra',OrdenCompraCRUD )
router.register(r'Pedido',PedidoCRUD )
router.register(r'Permiso',PermisoCRUD )
router.register(r'Producto',ProductoCRUD )
router.register(r'Proveedor',ProveedorCRUD )
router.register(r'Rol',RolCRUD )
router.register(r'RolHasPermiso',RolHasPermisoCRUD )
router.register(r'Sabor',SaborCRUD )
router.register(r'SaborHasProducto',SaborHasProductoCRUD )
router.register(r'TipoMovimiento',TipoMovimientoCRUD )
router.register(r'Usuario',UsuarioCRUD )
router.register(r'Venta',VentaCRUD )


urlpatterns=[
    path('',include(router.urls)),
]