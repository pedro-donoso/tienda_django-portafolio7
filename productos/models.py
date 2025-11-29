# productos/models.py
from django.db import models

# Modelo sin relaciones


class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad = models.IntegerField()
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre

# Modelo con relaciones


class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField(blank=True)

    def __str__(self):
        return self.nombre



class PerfilCliente(models.Model):  # uno a uno
    cliente = models.OneToOneField(Cliente, on_delete=models.CASCADE)
    telefono = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return f"Perfil de {self.cliente.nombre}"



class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='pedidos')  # 1 a muchos
    productos = models.ManyToManyField(Producto, related_name='pedidos')  # muchos a muchos
    fecha = models.DateField(auto_now_add=True)
    numero = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return f"Pedido {self.numero}"
