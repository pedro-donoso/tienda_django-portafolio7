# views.py
from django.views.generic import ListView

from django.utils import timezone

from .models import Pedido, Cliente

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