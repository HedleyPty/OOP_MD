from django.shortcuts import render
from .models import Capitulo, Contenido

# Create your views here.
def index(request,capitulo="2"):
    capt=Capitulo.objects.filter(id=capitulo)[0]
    nombre=capt
    contenido=Contenido.objects.filter(capitulo=capt)
    titulo=contenido[0].titulo
    imagen=contenido[0].imagen
    contenido1=contenido[0].contenido1
    contenido2=contenido[0].contenido2
    return render(request,
                    "index.html",
                    context= {"nombre":nombre,
                              "titulo":titulo,
                              "contenido1": contenido1,
                              "contenido2": contenido2,
                              "contenidos_todos":contenido,
                              "imagen":imagen})

