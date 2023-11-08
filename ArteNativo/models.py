from django.db import models

class Clientes(models.Model):
    app_label = 'ArteNativo'
    IdClientes = models.CharField(max_length=13)
    Nombre = models.CharField(max_length=100)
    Direccion = models.CharField(max_length=100)
    Telefono = models.CharField(max_length=12)
    email = models.EmailField()

class Productos(models.Model):
    app_label = 'ArteNativo'
    idProducto = models.CharField(max_length=13)
    Descripcion = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=0)
    stock = models.PositiveIntegerField()
    
class Ventas(models.Model):
    app_label = 'ArteNativo'
    cliente = models.ForeignKey(Clientes, on_delete=models.CASCADE, related_name='ventas_NombreCliente')
    producto = models.ForeignKey(Productos, on_delete=models.CASCADE, related_name='ventas_NombreProducto')
    fecha = models.DateField()
    cantidad = models.PositiveIntegerField()