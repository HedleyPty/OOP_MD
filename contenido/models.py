from django.db import models

# Create your models here.
class Contenido(models.Model):
    titulo=models.CharField(default="", max_length=25)
    contenido1=models.CharField(default="", max_length=300)
    titulo=models.ImageField(null=True)
