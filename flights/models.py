from django.db import models

class Flight(models.Model):
    FLIGHT_TYPES = [
        ('Nacional', 'Nacional'),
        ('Internacional', 'Internacional'),
    ]
    
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=15, choices=FLIGHT_TYPES)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f"{self.nombre} - {self.tipo}"
