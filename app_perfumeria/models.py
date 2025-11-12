from django.db import models
from decimal import Decimal

# ===============================
# MODELO: EMPLEADO
# ===============================
class Empleado(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    puesto = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    fecha_nacimiento = models.DateField(blank=True, null=True)        # Campo editable
    fecha_contratacion = models.DateField(blank=True, null=True)      # Campo editable
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

# ===============================
# MODELO: CLIENTE
# ===============================
class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    direccion = models.CharField(max_length=250, blank=True, null=True)
    fecha_registro = models.DateField(auto_now_add=True)
    empleado = models.ForeignKey(
        Empleado, on_delete=models.SET_NULL, blank=True, null=True, related_name='clientes_atendidos'
    )
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
# ===============================
# MODELO: VENTA PRODUCTO
# ===============================
class VentaProducto(models.Model):
    nombre_producto = models.CharField(max_length=150)
    descripcion = models.TextField(blank=True, null=True)
    cantidad = models.PositiveIntegerField(default=1)
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    total = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    fecha_venta = models.DateField(auto_now_add=True)

    # Relaciones
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='ventas')
    empleados = models.ManyToManyField(Empleado, related_name='ventas_asociadas')

    def save(self, *args, **kwargs):
        # Convierte cantidad y precio a tipos correctos antes de multiplicar
        cantidad_int = int(self.cantidad)
        precio_decimal = Decimal(self.precio_unitario)
        self.total = cantidad_int * precio_decimal
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.nombre_producto} - {self.cliente}"
