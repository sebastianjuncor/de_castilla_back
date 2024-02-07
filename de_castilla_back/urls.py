from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include('api.urls')),
    path('pedidos/',include('pedidos.urls')),
    path('usuarios/',include('usuarios.urls')),
    path('ventas/',include('usuarios.urls')),
]
