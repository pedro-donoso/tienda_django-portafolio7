# productos/urls.py
from django.urls import path

from .views import (
    ProductoListView, ProductoCreateView,
    ProductoUpdateView, ProductoDeleteView,
    PedidoListView, PedidosPorClienteView
)

urlpatterns = [
    # CRUD Producto
    path('productos/', ProductoListView.as_view(), name='producto_list'),
    path('productos/crear/', ProductoCreateView.as_view(), name='producto_create'),
    path('productos/<int:pk>/editar/', ProductoUpdateView.as_view(), name='producto_update'),
    path('productos/<int:pk>/eliminar/', ProductoDeleteView.as_view(), name='producto_delete'),

    # Pedidos
    path('pedidos/', PedidoListView.as_view(), name='pedido_list'),
    path('pedidos/cliente/<int:cliente_id>/', PedidosPorClienteView.as_view(), name='pedidos_por_cliente'),
]
