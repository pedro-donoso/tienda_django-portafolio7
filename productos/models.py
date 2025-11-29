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


class PerfilCliente(models.Model):  # Ejemplo OneToOne (1–1)
    cliente = models.OneToOneField(Cliente, on_delete=models.CASCADE)
    telefono = models.CharField(max_length=20, blank=True)


class Pedido(models.Model):
    cliente = models.ForeignKey(  # 1 cliente → muchos pedidos (1–N)
        Cliente,
        on_delete=models.CASCADE,
        related_name='pedidos'
    )
    productos = models.ManyToManyField(  # N–N
        Producto,
        related_name='pedidos'
    )
    fecha = models.DateField(auto_now_add=True)
    numero = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return f"Pedido {self.numero}"
