from django.urls import path

from .views import (
    HomeView,
    ProductoListView, ProductoCreateView,
    ProductoUpdateView, ProductoDeleteView,
    ClienteListView, ClienteCreateView,
    ClienteUpdateView, ClienteDeleteView,
    PedidoListView, PedidoCreateView,
    PedidoUpdateView, PedidoDeleteView,
    PedidosPorClienteView,
)

urlpatterns = [
    # Home
    path('', HomeView.as_view(), name='home'),

    # Clientes
    path('clientes/', ClienteListView.as_view(), name='cliente_list'),
    path('clientes/crear/', ClienteCreateView.as_view(), name='cliente_create'),
    path('clientes/<int:pk>/editar/', ClienteUpdateView.as_view(), name='cliente_update'),
    path('clientes/<int:pk>/eliminar/', ClienteDeleteView.as_view(), name='cliente_delete'),

    # Productos
    path('productos/', ProductoListView.as_view(), name='producto_list'),
    path('productos/crear/', ProductoCreateView.as_view(), name='producto_create'),
    path('productos/<int:pk>/editar/', ProductoUpdateView.as_view(), name='producto_update'),
    path('productos/<int:pk>/eliminar/', ProductoDeleteView.as_view(), name='producto_delete'),

    # Pedidos
    path('pedidos/', PedidoListView.as_view(), name='pedido_list'),
    path('pedidos/crear/', PedidoCreateView.as_view(), name='pedido_create'),
    path('pedidos/<int:pk>/editar/', PedidoUpdateView.as_view(), name='pedido_update'),
    path('pedidos/<int:pk>/eliminar/', PedidoDeleteView.as_view(), name='pedido_delete'),

    # Pedidos por cliente (consultas ORM)
    path('pedidos/cliente/<int:cliente_id>/', PedidosPorClienteView.as_view(), name='pedidos_por_cliente'),
]
