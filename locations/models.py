
# Create your models here.
from django.db import models

class Escuela(models.Model):
    nombre = models.CharField(max_length=100)
    slug = models.SlugField(unique=True) # Para la URL (ej: campusgo.com/escom)
    descripcion = models.TextField(blank=True)
    latitud_centro = models.FloatField() # Para centrar el mapa de Mapbox
    longitud_centro = models.FloatField()

    def __str__(self):
        return self.nombre

class Categoria(models.Model):
    nombre = models.CharField(max_length=50) # Ej: Baños, Salones, Auditorios
    icono = models.CharField(max_length=20, help_text="Emoji o nombre de icono") 

    def __str__(self):
        return self.nombre

class PuntoInteres(models.Model):
    escuela = models.ForeignKey(Escuela, on_delete=models.CASCADE, related_name='puntos')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100) # Ej: "Salón 1101" o "Baños Planta Baja"
    piso = models.IntegerField(default=0)
    latitud = models.FloatField()
    longitud = models.FloatField()

    def __str__(self):
        return f"{self.nombre} - {self.escuela.nombre}"