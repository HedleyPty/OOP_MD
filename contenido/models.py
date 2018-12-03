from django.db import models
from django.contrib.auth.models import User
from  django.contrib.postgres.fields import JSONField

class Estudiante(User):
    Aprobados=JSONField()
    

class Capitulo(models.Model):
    nombre=models.CharField(default="", max_length=20)
    
    
class Contenido(models.Model):
    capitulo=models.ForeignKey(Capitulo, on_delete=models.CASCADE, default="")
    titulo=models.CharField(default="", max_length=25)
    contenido1=models.CharField(default="", max_length=300)
    imagen=models.ImageField(null=True)