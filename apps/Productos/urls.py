from django.urls import path
from apps.Productos.views import listado, categorias
urlpatterns = [
    path('listado',listado),
    path('categorias', categorias),
]
