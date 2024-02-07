from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('pedidos/',include('pedidos.urls')),
    path('usuarios/',include('usuarios.urls')),
    path('ventas/',include('usuarios.urls')),
    path('proveedores/',include('proveedores.urls')),
    path('inventarios/',include('inventarios.urls')),
]
