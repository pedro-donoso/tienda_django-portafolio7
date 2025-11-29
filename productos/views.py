# productos/views.py
from django.views.generic import (
    ListView, CreateView, UpdateView, DeleteView
)
from django.urls import reverse_lazy

from django.db.models import Sum, Count

from .models import Producto, Pedido


# CRUD de Producto


class ProductoListView(ListView):
    model = Producto
    template_name = 'productos/producto_list.html'  # lista


class ProductoCreateView(CreateView):
    model = Producto
    fields = ['nombre', 'precio', 'cantidad', 'descripcion']
    template_name = 'productos/producto_form.html'  # crear/editar
    success_url = reverse_lazy('producto_list')


class ProductoUpdateView(UpdateView):
    model = Producto
    fields = ['nombre', 'precio', 'cantidad', 'descripcion']
    template_name = 'productos/producto_form.html'  # crear/editar
    success_url = reverse_lazy('producto_list')


class ProductoDeleteView(DeleteView):
    model = Producto
    template_name = 'productos/producto_confirm_delete.html'
    success_url = reverse_lazy('producto_list')


# Listado de pedidos (muestra relaciones)


class PedidoListView(ListView):
    model = Pedido
    template_name = 'pedidos/pedido_list.html'


class PedidoCreateView(CreateView):
    model = Pedido
    fields = ['numero', 'cliente', 'productos']
    template_name = 'pedidos/pedido_form.html'
    success_url = reverse_lazy('pedido_list')


class PedidoUpdateView(UpdateView):
    model = Pedido
    fields = ['numero', 'cliente', 'productos']
    template_name = 'pedidos/pedido_form.html'
    success_url = reverse_lazy('pedido_list')


class PedidoDeleteView(DeleteView):
    model = Pedido
    template_name = 'pedidos/pedido_confirm_delete.html'
    success_url = reverse_lazy('pedido_list')

# Pedidos por cliente y rango de fechas (filter, exclude, annotate)


class PedidosPorClienteView(ListView):
    model = Pedido
    template_name = 'pedidos/pedidos_cliente.html'

    def get_queryset(self):
        cliente_id = self.kwargs.get('cliente_id')
        fecha_inicio = self.request.GET.get('inicio')
        fecha_fin = self.request.GET.get('fin')

        qs = Pedido.objects.filter(cliente_id=cliente_id)

        if fecha_inicio and fecha_fin:
            qs = qs.filter(fecha__range=[fecha_inicio, fecha_fin])

        # ejemplo de exclude y annotate
        qs = (
            qs.exclude(productos__cantidad=0)
              .annotate(
                  total_productos=Count('productos'),
                  total_items=Sum('productos__cantidad')
            )
        )
        return qs
