from django.urls import path
from .views import index

urlpatterns = [
     path('<int:capitulo>/', index),
]
