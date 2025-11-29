from django.db import models

# Modelo sin relaciones


class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad = models.IntegerField()

    def __str__(self):
        return self.nombre

# Modelo Cliente (para relaciones)


class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField(blank=True)

    def __str__(self):
        return self.nombre

# Modelo Pedido con relaciones


class Pedido(models.Model):
    # uno a muchos: un cliente puede tener muchos pedidos
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    # muchos a muchos: un pedido puede tener muchos productos
    productos = models.ManyToManyField(Producto)
    fecha = models.DateField(auto_now_add=True)
    numero = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return f"Pedido {self.numero}"
