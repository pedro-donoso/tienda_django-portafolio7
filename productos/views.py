# views.py
from django.views.generic import ListView, UpdateView,DeleteView

from django.urls import reverse_lazy

from django.utils import timezone

from .models import Pedido, Cliente, Producto

from django.db.models import Sum, Count


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

        return qs


class PedidosResumenView(ListView):
    model = Pedido
    template_name = 'pedidos/resumen.html'

    def get_queryset(self):
        return (
            Pedido.objects
            .exclude(productos__cantidad=0)          # exclude()
            .annotate(total_productos=Count('productos'),
                      total_items=Sum('productos__cantidad'))  # annotate()
        )


class ProductoListView(ListView):
    model = Producto
    template_name = 'productos/producto_list.html'


class ProductoCreateView(CreateView):
    model = Producto
    fields = ['nombre', 'precio', 'cantidad', 'descripcion']
    template_name = 'productos/producto_form.html'
    success_url = reverse_lazy('producto_list')


class ProductoUpdateView(UpdateView):
    model = Producto
    fields = ['nombre', 'precio', 'cantidad', 'descripcion']
    template_name = 'productos/producto_form.html'
    success_url = reverse_lazy('producto_list')


class ProductoDeleteView(DeleteView):
    model = Producto
    template_name = 'productos/producto_confirm_delete.html'
    success_url = reverse_lazy('producto_list')