from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .controllers.Permiso import PermisoCRUD
from .controllers.Rol import RolCRUD
from .controllers.RolHasPermiso import RolHasPermisoCRUD
from .controllers.Usuario import UsuarioCRUD

router = DefaultRouter()
router.register(r'permisos',PermisoCRUD )
router.register(r'roles',RolCRUD )
router.register(r'rol_has_permiso',RolHasPermisoCRUD )
router.register(r'usuarios',UsuarioCRUD )
