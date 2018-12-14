from django.shortcuts import render
from .models import Capitulo 

# Create your views here.
def index(request,capitulo):
    capt=Capitulo.objects.filter(id=capitulo)
    nombre=capt[0].nombre
    return render(request, "index.html", context= {"nombre":nombre})

