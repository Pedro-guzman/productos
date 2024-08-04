from django.db import models

class Productos(models.Model):
    codigo_barras = models.CharField(max_length=100, unique=True) 
    producto = models.CharField(max_length=50, blank=False, null=False) 
    costo = models.DecimalField(max_digits=10, decimal_places=2) 
    venta = models.DecimalField(max_digits=10, decimal_places=2) 
    cantidad = models.IntegerField(blank=True)
    
    def __str__(self):
        return self.producto
