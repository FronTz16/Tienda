from django.db import models

# Create your models here.
class Categorias(models.Model):
    nombre_categoria=models.CharField(max_length=50)
    fecha_creacion=models.DateField(default='2000-01-01')