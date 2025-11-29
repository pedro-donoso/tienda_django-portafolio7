from django.urls import path

from .views import (
    ProductoListView, ProductoCreateView,
    ProductoUpdateView, ProductoDeleteView,
    PedidoListView, PedidoCreateView,
    PedidoUpdateView, PedidoDeleteView,
)

urlpatterns = [
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
]
