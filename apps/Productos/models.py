from django.db import models

# Create your models here.
class productos(models.Model):
    nombre_producto= models.CharField(max_length=50)
    descripcion=models.CharField(max_length=50)
    costo = models.IntegerField(default='0')
    disponible= models.IntegerField(default='0')
    num_existencias=models.IntegerField(default='0')

class categorias(models.Model):
    nombre_categoria=models.CharField(max_length=50)
    fecha_creacion=models.DateField(default='2000-01-01')