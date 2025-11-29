from django.contrib import admin

from .models import Producto, Cliente, Pedido


@admin.register(Producto)


class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'cantidad')
    search_fields = ('nombre',)


@admin.register(Cliente)


class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'correo')


@admin.register(Pedido)


class PedidoAdmin(admin.ModelAdmin):
    list_display = ('numero', 'cliente', 'fecha')
    list_filter = ('fecha',)
