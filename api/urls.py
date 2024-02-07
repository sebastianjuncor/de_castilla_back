from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .controllers.Calificacion import CalificacionCRUD
from .controllers.Categoria import CategoriaCRUD
from .controllers.DetalleOc import DetalleOcCRUD
from .controllers.DetalleVenta import DetalleVentaCRUD
from .controllers.EstadoInsumo import EstadoInsumoCRUD
from .controllers.EstadoOc import EstadoOcCRUD
from .controllers.Historico import HistoricoCRUD
from .controllers.Insumo import InsumoCRUD
from .controllers.Inventario import InventarioCRUD
from .controllers.OcHasProveedor import OcHasProveedorCRUD
from .controllers.OrdenCompra import OrdenCompraCRUD
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
router.register(r'calificaciones',CalificacionCRUD )
router.register(r'categorias',CategoriaCRUD )
router.register(r'detalles_oc',DetalleOcCRUD )
router.register(r'detalles_venta',DetalleVentaCRUD )
router.register(r'estados_insumo',EstadoInsumoCRUD )
router.register(r'estados_oc',EstadoOcCRUD )
router.register(r'historicos',HistoricoCRUD )
router.register(r'insumos',InsumoCRUD )
router.register(r'inventarios',InventarioCRUD )
router.register(r'oc_has_roveedor',OcHasProveedorCRUD )
router.register(r'ordenes_compra',OrdenCompraCRUD )
router.register(r'permisos',PermisoCRUD )
router.register(r'productos',ProductoCRUD )
router.register(r'proveedores',ProveedorCRUD )
router.register(r'roles',RolCRUD )
router.register(r'rol_has_permiso',RolHasPermisoCRUD )
router.register(r'sabores',SaborCRUD )
router.register(r'sabores_has_producto',SaborHasProductoCRUD )
router.register(r'tipos_movimiento',TipoMovimientoCRUD )
router.register(r'usuarios',UsuarioCRUD )
router.register(r'ventas',VentaCRUD )


urlpatterns=[
    path('',include(router.urls)),
]