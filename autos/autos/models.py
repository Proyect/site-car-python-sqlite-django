from django.db import models

class Vehicle(models.Model):
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    anio = models.IntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    motor = models.CharField(max_length=50)
    transmision = models.CharField(max_length=50, choices=[
        ('Manual', 'Manual'),
        ('Automática', 'Automática'),
    ])
    combustible = models.CharField(max_length=50, choices=[
        ('Gasolina', 'Gasolina'),
        ('Diésel', 'Diésel'),
        ('Eléctrico', 'Eléctrico'),
        ('Híbrido', 'Híbrido'),
    ])
    descripcion = models.TextField(blank=True, null=True)
    imagen_url = models.URLField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.marca} {self.modelo} ({self.anio})"    
    
class Img(models.Model):
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    url = models.CharField(max_length=200 )
    state = models.CharField(max_length=50, choices=[("on","on"),("off","off")],default=["on"])
    
    def __str__(self):
        return f"{self.marca} {self.modelo} ({self.url} {self.state})" 
    
class Description(models.Model):
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    title = models.CharField(max_length=200)
    content = models.TextField()
    state = models.CharField(max_length=50, choices=[("on","on"),("off","off")],default=["on"])

    def __str__(self):
        return f"{self.marca} {self.modelo} {self.title} {self.content}"