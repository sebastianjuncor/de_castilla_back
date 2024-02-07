from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .controllers.Categoria import CategoriaCRUD
from .controllers.EstadoInsumo import EstadoInsumoCRUD
from .controllers.Historico import HistoricoCRUD
from .controllers.Insumo import InsumoCRUD
from .controllers.Inventario import InventarioCRUD
from .controllers.Producto import ProductoCRUD
from .controllers.Sabor import SaborCRUD
from .controllers.SaborHasProducto import SaborHasProductoCRUD
from .controllers.TipoMovimiento import TipoMovimientoCRUD

router = DefaultRouter()
router.register(r'categorias',CategoriaCRUD )
router.register(r'estados_insumo',EstadoInsumoCRUD )
router.register(r'historicos',HistoricoCRUD )
router.register(r'insumos',InsumoCRUD )
router.register(r'inventarios',InventarioCRUD )
router.register(r'productos',ProductoCRUD )
router.register(r'sabores',SaborCRUD )
router.register(r'sabores_has_producto',SaborHasProductoCRUD )
router.register(r'tipos_movimiento',TipoMovimientoCRUD )


urlpatterns=[
    path('',include(router.urls)),
]