from django.db import models

# Database - Modelo Flight con atributos requeridos
class Flight(models.Model):
    TIPOS_VUELO = [
        ('Nacional', 'Nacional'),
        ('Internacional', 'Internacional'),
    ]
    
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200)
    tipo = models.CharField(max_length=20, choices=TIPOS_VUELO)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        ordering = ['precio']  # Ordenados por precio
